# # Third Party
# import librosa
# import numpy as np

# # ===============================================
# #       code from Arsha for loading data.
# # ===============================================
# def load_wav(vid_path, sr, mode='train'):
#     wav, sr_ret = librosa.load(vid_path, sr=sr)
#     assert sr_ret == sr
#     if mode == 'train':
#         extended_wav = np.append(wav, wav)
#         if np.random.random() < 0.3:
#             extended_wav = extended_wav[::-1]
#         return extended_wav
#     else:
#         extended_wav = np.append(wav, wav[::-1])
#         return extended_wav


# def lin_spectogram_from_wav(wav, hop_length, win_length, n_fft=1024):
#     linear = librosa.stft(wav, n_fft=n_fft, win_length=win_length, hop_length=hop_length) # linear spectrogram
#     return linear.T


# def load_data_old(path, win_length=400, sr=16000, hop_length=160, n_fft=512, spec_len=250, mode='train'):
#     wav = load_wav(path, sr=sr, mode=mode)
#     linear_spect = lin_spectogram_from_wav(wav, hop_length, win_length, n_fft)
#     mag, _ = librosa.magphase(linear_spect)  # magnitude
#     mag_T = mag.T
#     freq, time = mag_T.shape
#     if mode == 'train':
#         randtime = np.random.randint(0, time-spec_len)
#         spec_mag = mag_T[:, randtime:randtime+spec_len]
#     else:
#         spec_mag = mag_T
#     # preprocessing, subtract mean, divided by time-wise var
#     mu = np.mean(spec_mag, 0, keepdims=True)
#     std = np.std(spec_mag, 0, keepdims=True)
#     print("\n\n\n",((spec_mag - mu) / (std + 1e-5)).shape,"\n\n\n")
#     return (spec_mag - mu) / (std + 1e-5)

import os
import cv2
import numpy as np
def load_data(path,dim_w=112,dim_h=112, win_length=400, sr=16000, hop_length=160, n_fft=512, spec_len=250, mode='train'):
    c=0
    # print(dim_w,"    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    ",dim_h,spec_len)
    big_arr=[]
    sub_arr=[]
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    while(success):
        image= cv2.resize(image,(dim_h,dim_w))
        sub_arr.append(image)
        success,image = vidcap.read() 
        c+=1
    while(c<spec_len):
        sub_arr.append(sub_arr[-1])
        c+=1
    
    # if(len(sub_arr)>0):
    big_arr=sub_arr[:spec_len]
    np_arr=np.asarray(big_arr)
    # print(np_arr.shape,"       GgggG")
    return np_arr
