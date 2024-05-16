def frequency_analysis(text):

    text = text.lower()

    frequency = {}

    for char in text:
        if char.isalpha(): 
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequency