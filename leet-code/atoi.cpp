int atoi(const char* number) {
    int ans = 0;

    // Check flag
    bool is_negative = false
    int idx = 0
    if (number[0] == '-') {
        is_negative = true;
        idx++
    } else if (number[0] == '+') {
        idx++
    }

    // Loop over digits in reverse order
    
    while (number[idx] != 0) {
        char digit = number[idx];

        if (digit < '0' || digit > '9')
            return ans;

        int digit_number = digit - '0';

        ans *= 10;
        ans += digit_number;

        idx++;
    }
    
    /*for (int idx = 0; idx < length; idx++) {
        char digit = number[length-idx-1];

        // TODO: Check value digit

        int digit_number = digit - '0'
        ans += digit_number * math.pow(10, idx)
    }*/

    return !is_negative ? ans : -ans;
}