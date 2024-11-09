def main() {
        var fs = 1000;
        var input = getRangeOfVector(0, 10000, 0.000125);
        var sep = getRangeOfVector(0, 1, 0.5);
        var pi = 3.14159265359;
        var getMultiplier = 2 * pi * 5;
        var getSinDuration = gain(input, getMultiplier);
        var signal = sin(getSinDuration );

        var noise = delay(signal, 5);
        var noisy_sig = signal + noise;
        var threshold = 0.8;
        var zeroOpt = zero_cross_threshold_opt(noisy_sig, threshold);
        print(noisy_sig);
        print(zeroOpt);
}
