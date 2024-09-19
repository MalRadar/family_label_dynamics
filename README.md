## Android Malware Family Labeling

### Overview
This study examines the challenges in labeling Android malware families, focusing on results in widely-used tools like AVClass and Euphony. 
Using a large dataset from Google Play and third-party markets, we reveal how these tools struggle with temporal inconsistencies, label evolution, and handling multi-family malware. 
Our findings highlight the need for improved labeling methods to ensure more reliable threat detection and security. 
The data used in this study are available to support further research and industry applications.

### VT scan reports:
Due to the data size limitation of Github, we put all the VT scan reports of samples on [Zenodo](https://zenodo.org/records/13790832).
It includes: (1) the first and second VT scans for the GPset; (2) the first and second VT scans for the 3rdset;
(3) the VT scan for the fused (multi-family) samples.

### paper-materials: 
This folder contains materials discussed in the paper's main content. 
Due to space limitations in the published version, several key elements, including figures, tables, and additional data, are provided here for reference. 
Each file is organized to complement specific sections of the paper and offer further insights into the findings.

### family-label-results:
This folder contains the family labeling results of the two datasets from AVClass and Euphony, respectively.

### multi-family sample analysis:
This folder contains materials related to Section 7 (Family Label of Multi-Family Samples).
```src``` includes scripts for app/family fusion process. 
```csv``` files store the labeling results from AVClass and Euphony. 
The VT scan reports of the fused apps are available on Zenodo.