from threading import Thread

import pyaudio
import wave
import numpy as np

from base.project import Project

CHUNK_SIZE = 4096
NORMALIZE = True
AUTO_CROP = 50
class Recorder:
    def __init__(self, project: Project):
        self.project = project

        self.sampling_rate = self.project._sampling_rate
        self.format = pyaudio.paInt16 if self.project._encoding == 2 else pyaudio.paInt32
        self.audio = pyaudio.PyAudio()

        self.recording = False
        self.playing = False

        self.buffer = b''

    def _open_stream(self):
        return self.audio.open(format=self.format,
                               channels=1,
                               rate=self.sampling_rate,
                               input=True,
                               frames_per_buffer=CHUNK_SIZE)

    def record(self):
        self.stream = self._open_stream()
        while self.recording:
            frames = self.stream.read(CHUNK_SIZE, exception_on_overflow=False)
            self.buffer += frames

    def start_recording(self):
        self.buffer = b''
        self.recording = True
        self.th = Thread(target=self.record, args=())
        self.th.start()
        
    def stop_recording(self):
        self.recording = False
        self.th.join()
        self.stream.stop_stream()
        self.stream.close()
        if NORMALIZE:
            self.buffer = normalize_audio(self.buffer, self.project._encoding)

    def play_audio(self):
        stream = self.audio.open(format=self.format,
                        channels=1,
                        rate=self.sampling_rate,
                        output=True)
        stream.write(self.buffer)

    def save_audio(self, file_path):
        wavefile = wave.open(file_path, 'wb')
        wavefile.setnchannels(1)
        wavefile.setsampwidth(self.project._encoding)
        wavefile.setframerate(self.project._sampling_rate)
        wavefile.writeframes(self.buffer)
        
    def clear_buffer(self):
        self.buffer = b''

    @property
    def audio_duration(self) -> float:
        buff_l = len(self.buffer)
        return buff_l / (self.sampling_rate * self.project._encoding) 

def normalize_audio(buffer: bytes, encoding, factor: float = 0.90) -> bytes:
    np_format = np.int16 if encoding == 2 else np.int32
    signal = np.frombuffer(buffer, dtype=np_format)[AUTO_CROP:-AUTO_CROP]
    max_value = np.iinfo(np_format).max
    max_sig = max(signal.max(), abs(signal.min()))
    if max_sig >= max_value * factor:
        return buffer
    signal_norm = signal * (max_value * factor) / max_sig
    signal_norm = signal_norm.astype(np_format)
    return signal_norm.tobytes()
    

def list_sources() -> list:
    audio = pyaudio.PyAudio()
    info = audio.get_host_api_info_by_index(0)
    num_device = info.get('deviceCount')
    devices = []
    for i in range(num_device):
        device = audio.get_device_info_by_host_api_device_index(0,i)
        if device.get('maxInputChannels') > 0:
            devices.append((len(devices), 
                           device.get('name'),
                           device.get('defaultSampleRate')))
    return devices