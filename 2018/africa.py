import scipy.io.wavfile as wav

datos = wav.read("africa.wav")

datos_out = datos[1][::-1]

wav.write("africa_sol.wav", datos[0], datos_out)



