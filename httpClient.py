import time
import requests

def main():
    # Replace 'your-raspberry-pi-ip' with the actual IP address of your Raspberry Pi
    url = 'http://192.168.81.100:8000/http'

    try:
        start_time = time.time()
        response = requests.get(url)
        if response.status_code == 200:
            end_time = time.time()
            http_time = end_time - start_time
            print(f"Request Latency: {http_time:.4f} seconds")
            print("Response:", response.text)
        else:
            print("Error: Request failed with status code", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
