import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

bytes_to_mbs = download/1000000
bytes_to_mbs2 = upload/1000000

x = round(bytes_to_mbs,2)
y = round(bytes_to_mbs2,2)

print("Downloading speed : ", x, "MBS")
print("Uploading speed : ", y, "MBS" )
