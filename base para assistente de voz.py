import speech_recognition as sr
#Função para ouvir e reconhecer a fala
#o import os para rodar comandos do cmd
import os
#variavel global para salvar a frase dita
ultima_frase_dita = ""


def cmd(comando_recebido):
    os.system('cmd /k '+comando_recebido)



def falar(texto_a_se_falado):
    #os.system('cmd /k  echo >script.vbs "CreateObject(""SAPI.SpVoice"").Speak(""'+texto_a_se_falado+'"") & script.vbs')
    import pyttsx3 
    engine = pyttsx3.init() 
    engine.say(texto_a_se_falado) 
    engine.runAndWait()

def fale(texto_a_ser_falado):
    falar(texto_a_ser_falado)

falar("Iniciando IÁ com sistema de reconhecimento de voz. Estou pronta para receber seus comandos. Por favor fale o que deseja.")
print("Iniciando IA com sistema de reconhecimento de voz. Estou pronta para receber seus comandos. Por favor fale o que deseja.")

def ouvir_microfone():
    try:
        #Habilita o microfone do usuário
        microfone = sr.Recognizer()
        
        #usando o microfone
        with sr.Microphone() as source:
            
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            print("Diga alguma coisa: ")
            
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
            
        try:
            
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')

            #ultima_frase_dita = frase
            
            #Retorna a frase pronunciada
            print("Você disse: " + frase)
            falar("Você disse: "+frase)
            
        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnkownValueError:
            print("Não entendi")
            falar("não entendi...")
            
        return frase
    except:
        print('Nenhum comando enviado')
        return ''


ouvir_microfone()

#criando um loop para esperar o comando desativar

ativar_1_desativar_0 = 0
while ativar_1_desativar_0 < 1:
    ultima_frase_dita = ouvir_microfone()
    if ultima_frase_dita == "parar":
        ativar_1_desativar_0 = 1
        fale('finalizando o processo da Iá.')
        print('finalizando IA')
    else:
        print("continuar escutando...")
        falar("continuo escutando")
        ouvir_microfone()
     


fale('Sistema finalizado')