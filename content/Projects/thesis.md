Title: The Abstraction of My Thesis
Date: 2014-05-30 02:13
Tags: Master Thesis, Cache Oriented Obfuscation, Malware, Obfuscation
Summary: It was the end of the long adventure, but at the end I managed to be done

There is no doubt that malicious software (malware) is one of the most important threat in computer security. With increasing of the information systems and computer network usage in the industrial and governmental infrastructures, their economy and impact over our society are increasing. According to Symantec's report in 2008, "The release rate of malicious code and other unwanted programs may be exceeding that of legitimate software applications." The worst of all, malware design is not as simple as how it was before. A few years ago, we saw countries who developed malware as a professorial weapon for their political benefits, and it would not be surprising if one of these weapons were seen in the corporate world soon. This malware was utilized with many camouflaging techniques (e.g. polymorphism, metamorphism, etc.) against the malware detection system.

Basically, the most of the camouflaging techniques obfuscate and hide the signatures to be stored safely in a non-volatile memory or disk, and before they started to run on the main memory, they deobfuscate the whole code to execute. Consequently, the detection systems have simply started to search the signatures in the main memory. In this thesis, we designed a way to raise the bar from "from disk to memory obfuscation" to "from disk to cache obfuscation". More specifically, we designed theoretical malware obfuscation methods for tightly coupled multi-processor systems which utilize caches as a private memory to evade main memory observer systems as well as other conventional static data analysis. In order to achieve this goal, we anticipated cache behaviours and exploited them as well as cache efficiency optimizations. With increasing deployment of multi-processor computing and other parallel processing devices, the implementation of local memories like NUMA and hierarchical caches are increasing in order to increase efficiency and performance and decrease power consumption, and this can be even the only reason which highlight our studies. Additionally, this thesis discusses the implementation issues which we can experience on cache coherent systems or the Harvard Architecture.