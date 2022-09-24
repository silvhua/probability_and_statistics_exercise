def indttest(nullhyp,data1,data2,alpha=0.05):
    """Check whether or not we reject a given null hypothesis
    Parameters:
        nullhyp: (string) Null hypothesis
        data1, data2: Panda series of the 2 samples to compare.
        alpha: (float, optional) P-value threshold for significance. Default is 0.05.
    """
    print('Null hypothesis tested: ',nullhyp)
    ttest = st.ttest_ind(data1,data2)
    print(ttest)
    if ttest[1]<alpha:
        print('Test result: Reject the null hypothesis; samples are significantly different.\n')
    else:
        print('Test result: Fail to reject the hypothesis H0.\n')
    return ttest[1]