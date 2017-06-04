from bart_api import BartApi

def bart_info():
    bart = BartApi()
    dbrk = bart.etd("DBRK")

    for x in dbrk:
        print(x['destination'])
        for train in x['estimates']:
            print(train['minutes'])
        print("******************")

if __name__ == "__main__":
    bart_info()
