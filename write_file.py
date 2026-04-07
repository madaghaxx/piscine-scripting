def to_do(data):
    with open("output.txt", "w") as file:
        for i in range(len(data)):
            date = data[i][0]
            formatted_date = date.strftime("%A %d %B %Y")
            # print(formatted_date+": "+data[i][1])
            file.write(formatted_date+": "+data[i][1]+"\n")