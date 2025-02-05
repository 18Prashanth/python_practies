writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)