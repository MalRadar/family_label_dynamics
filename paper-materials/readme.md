## Paper Artifacts and Supplementary Materials

This folder contains supplementary materials and artifacts related to the paper. 
Due to space limitations in the published version, several key elements, including figures, tables, and additional data, are provided here for reference. 
Each file is organized to complement specific sections of the paper and offer further insights into the findings.

1. **evolved-ratio-cdf.pdf**: This is a figure showing the overall CDF distribution of each family's evolved ratio, 
with results from the two systems presented separately. It illustrates the content discussed in the section 4.2.3 of the published paper.

2. **euphony-detected-ratio.png**: This is a figure showing the detected ratio in multi-family apps for each malware family 
with respect to the Euphony results, the counterpart to the Figure 4 in the published paper. 
Particularly, 7 families in AVClass results and 9 families in Euphony results have a detected ratio of 0, meaning that none of the fused apps including these families were identified as such, indicating a low priority in antivirus detection.

3. A table showing examples of apps (MD5) and their labeled families for each type, corresponding to the section 7.2.1 of the published paper.
This table provides examples of fused apps, along with their associated host and rider apps, as well as the family labels assigned to each. 
The fused apps are categorized into four types based on the consistency of their family labels with those of the host and rider apps.

| **Type** | **host app (host family)** | **rider app (rider family)** | **fused app (fused family)** |
|----------|----------------------------|------------------------------|------------------------------|
| ①        | 940f562ded0dd9c48235fb9ea738f405 (anubis)   | 2e5b635445a3bc0237ee42b51e8de6db (riltok)   | 5d34108157da1de84c6a744e4dcd4fac (anubis)   |
| ②        | fdda9a4b443a7c18a43946e402284b75 (eventbot) | 43680d1914f28e14c90436e1d42984e2 (dvmap)    | e51fba95cf069051801acd80fb465e23 (dvmap)    |
| ③        | 09991069cecd942abca58be77742337d (asacub)   | 4c0b9a665a5a1f5dccb67cc7ec18da54 (fakeapp)  | 555559edd22f31bc34244a7712c31487 (bankbot)  |
| ④        | cadb40c31f9455fc3a3eeb7c672a2e35 (monokle)  | 4c0b9a665a5a1f5dccb67cc7ec18da54 (fakeapp)  | 90bb07429787bb82442110a4034eca5d (-)        |

4. **family-alias-list.txt**: The list of family aliases that supports the analysis presented in the section 6 of the published paper.
Each line represents all the aliases corresponding to the same family.