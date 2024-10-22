def main() {
    var input_data = [1,1,1,0,1,1,1,0];
    print(input_data);
    var modulated_symbols = qam_modulate(input_data);
    print(modulated_symbols);
    # var decoded_data = qam_demodulate(modulated_symbols);
    # print(decoded_data);
}
