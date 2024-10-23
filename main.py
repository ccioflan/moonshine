import argparse

from moonshine import transcribe

def main():

    parser = argparse.ArgumentParser(prog='Moonshine wav2text')
    parser.add_argument('--wav', type=str, default=None, help="Path to .wav to transcribe")  
    parser.add_argument('--model', type=str, default=None, help="Model size")  

    args = parser.parse_args()

    print (transcribe(args.wav, 'moonshine/'+args.model))

if __name__ == "__main__":
    main()