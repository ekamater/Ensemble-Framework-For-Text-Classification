This folder describes the datasets we used for our experiments.

### CLEFIP-2011-0.54M
The CLEFIP-0.54M contains the English patents of the CLEF-IP 2011 test collection, which have been extracted with the condition to have (i.e., not being empty) the main classification code, the EN abstract, the EN description, the EN claims, the EN title, the applicants, and the inventors. In addition to the main classification code, all (main and further) IPC classification codes at the subclass (third) level of the IPC 5+ level hierarchy are available. The dataset contains 541,131 patents classified in 731 main (and 810 main and further) subclass codes. Moreover, the text of the EN abstract, the EN description, and the EN claims has undergone a pre-processing, removing any character that is not alphabetic and English stop words.

For the CLEFIP-2011-0.54M, we used the latest version of the dataset uploaded in the following link: https://github.com/ekamater/CLEFIP-0.54M.

### WIPO-alpha
The WIPO-alpha is an English patent database issued in 2002 by the World Intellectual Property Organization (WIPO). It is a data collection of about 75K XML documents distributed over 30,000 codes in the fifth level and 5,500 codes in the fourth level, e.g., there is only one patent with the “A01C00502” code in the fifth level and seven patents with the “A01C005” code in the fourth level. For our experiments, we use the codes of the third level, known as subclass codes, which amount to 451 main codes and 633 all codes (main and further).

For the WIPO-alpha, we used the dataset issued in 2002 by the World Intellectual Prop-erty Organization (WIPO). The dataset has stopped to be provided by WIPO. You can directly contact us to give you access to this. Moreover, the folder "wipo-alpha" provides the code we used to transfer the data of patent xml files into a mysql database and the final subfields we used containing the main classification, the ipcr codes and the abstract text. 

### USPTO-2M
The USPTO-2M is a large-scale patent classification dataset made publicly available by Li et al [1](https://link.springer.com/article/10.1007/s11192-018-2905-5). The dataset includes the title, the abstract, and the subclass labels (multi-label) for each patent. The dataset contains 2,000,147 patents classified in 637 categories from 2006 to 2015. The same or subparts of this dataset have been used by other studies, such as in Roudsari et al. [2](https://link.springer.com/article/10.1007/s11192-021-04179-4), which removes the low-represented labels with a frequency of less than 100 documents and finally considers 544 labels.

For the USPTO-2M (Arousha), the initial USPTO-2M is available here: [USPTO-2M](https://github.com/JasonHoou/USPTO-2M). We used a subpart of the USPTO-2M sorting out the labels that contained less than 100 documents as documented by Roudsari et al. A link will be published after getting the aproval of Dr. Arousha Haghighian Roudsari.

### Web of Science (WOS-5736, WOS-11967, and WOS-46985)
The Web of Science (WOS) is a document classification dataset of 46,985 scientific papers with 134 categories and 7 parent categories, which have been made available by the Web of Science. Each document contains two fields, the abstract, and the keywords, provided by the authors. The WOS-5736 and WOS-11967 are two subsets of the WOS-46985. The WOS-11967 contains 11,967 documents with 35 categories and 7 parent categories and the WOS-5736 contains 5736 documents with 11 categories and 3 parent categories.

For the WoS, we used the dataset from excel files provided in the following link: https://data.mendeley.com/datasets/9rw3vkcfy4/6.

### EURLEX57K
The EURLEX57K [3](https://aclanthology.org/P19-1636/) contains 57K English EU legislative documents from the EUR-LEX portal tagged with ∼4.2K labels (concepts) from the European Vocabulary (EUROVOC). Each legislative document is provided in a JSON file containing information for a legal act (EU Directive, Regulation, Decision), as published in the Eur-Lex portal. The entire content of each legal act can be represented solely by its title, header, recitals, main body, and attachments.

For the EURLEX57K, we used the dataset as it is provided in the following link: https://github.com/iliaschalkidis/lmtc-eurlex57k. We transfered the dataset in a mysql database and then we tranformed the train, dev and test tables into csv files. The folder "eurlx57k" provides the code we used to transfer the data of patent json files into a mysql database and the final csv files we used for the experiments. 
