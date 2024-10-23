def main() {
    var input_data = [1,1,1,0,1,1,1,0];
    print(input_data);
    var real, imagine = qam_modulate(input_data);
    print(real);
    print(imagine);
    # var real_part = [1, 1, 1, 1];
    # var img_part = [1, -1, 1, -1];
    # var decoded_data = qam_demodulate(real_part, img_part);
    # print(decoded_data);
}
