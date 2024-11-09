def main() {
        var testcase = [1, -0.000000001, 0.00000001, 0, 0, -3, 0, 0, 0, 2, 0, 0, 2];
        # cross 2
        var threshold = 0;
        # var ans = zeroCrossCount(testcase);
        var ans = zero_cross_threshold_opt(testcase, threshold);
        print(ans);
}
