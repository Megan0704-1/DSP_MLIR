def main() {
        var fs = 1000;
        var input = getRangeOfVector(0, 100000000, 0.000137);
        var sep = getRangeOfVector(0, 1, 0.5);
        var pi = 3.14159265359;
        var getMultiplier = 2 * pi * 5;
        var getSinDuration = gain(input, getMultiplier);
        var signal = sin(getSinDuration );

        var noise = delay(signal, 5);
        var noisy_sig = signal + noise;
        var threshold = 0.8;
        # print(sep);
        var GetThresholdReal = threshold( noisy_sig , threshold);
        # print(GetThresholdReal);
        var zcr = zeroCrossCount(GetThresholdReal);
        print(zcr);
        # print(noisy_sig);
}
