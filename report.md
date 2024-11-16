## Previous writing

Three datasets were provided, of which two were labeled as training and one test. The smaller of the training datasets, called \textit{species\_train.npz}, included sightings of 500 species with a total of \num{272037} sighting locations, while the test set \textit{species\_test.npz} contained \num{1706646} locations for the same species. The larger training dataset \textit{species\_train\_extra.npz} however, contained \num{1067592} sightings for \num{1918} different species. Both training datasets contained only positive data of species recordings, and we primarily used \textit{species\_train.npz} for the project, unless otherwise mentioned.

\label{section:network_analysis}
The location data provided is useful for analyzing patterns of habitation, but has limitations to what insights can be drawn, particularly when considering that this dataset was not tagged with timestamps. We thus devised a methodology to provide richer ecological analysis for a given species, with the aim to provide researchers the ability to visualize ecosystems for a given set of records in a specific habitat. This could help researchers in their conservation efforts, allowing the identification of necessary criteria for a target rehabilitation ecosystem, in order to ease the selection of where and how to best intervene. In fact, the species' traits data also included interesting information about how the various animals relates with each other. In particular, for some of the analyzed species the EOL reported their interactions with other biological beings such as viruses, plants, and other animals too. A total of 18 different types of interaction (e.g., 'are eaten by', 'prey on', 'are parasitized by') were reported in the EOL for the 500 species in analysis, sometimes associating them to other animals in the same original dataset. Therefore, we leveraged the above information to reconstruct some ecosystems of interest, conceived as networks of species interconnected by relations of the aforementioned type. This helped us to have a wider view on the results obtained, giving a causal meaning to animals' co-presences.

Firstly, we built an interaction framework spanning all and only the species in the original dataset; then, we applied the same procedure on subsections animals based on the locations clusters previously produced, obtaining especially representative outputs with habitat sub-graphs (i.e., relation networks of species sharing a particular area characterized by geographical cohesion and environmental uniformity). The latter were also enlarged by including species among the main 500 analyzed but with no sightseeing record in the specific habitat —displayed as outlined nodes— and biological entities not among these original animals —reported as nodes labeled with the relevant scientific name only. The nodes are color-coded by taxonomy class and sized proportionally to their number of records in the relevant area; the edge between represent the most crucial interaction they entertain, prioritizing the interactions type we conceived as most important —as ordered in the legend.

\begin{figure}[h]
    \centering
    \begin{minipage}{0.46\textwidth}
        \centering
        \includegraphics[height=0.33\textheight,keepaspectratio]{aml_latex_template (1)/aml_latex_template/figures/co_occurring_net.pdf}
        \caption{Example of ecosystem core shared by a couple of highly co-occurring species}
        \label{fig:co_occurring_net}
    \end{minipage}
    \hfill
    \begin{minipage}{0.46\textwidth}
        \centering
        \includegraphics[height=0.33\textheight,keepaspectratio]{aml_latex_template (1)/aml_latex_template/figures/amazon_rainforest_net.pdf}
        \caption{Most populated Amazon rain-forest ecosystem's connected core}
        \label{fig:amazon_rainforest_net}
    \end{minipage}
\end{figure}

The obtained graphs are quite sparse and disconnected with respect to what one would expect from an actual natural ecosystem, due to the application of our method to the 500 analyzed species' relational information only: further elements not present among the target of these main animals' interaction data are not considered, thus only weak paths including a single additional specie are displayable to deepen the understanding of animals' correlation. Nevertheless, we were able to observe possible reasons for some of the most location-correlated species' co-occurrence by considering their roles in some shared habitats (e.g., Anaxyrus boreas and Taricha torosa in fig.~\ref{fig:co_occurring_net}). Moreover, highly connected nodes appear which have 0 records or are not among the main 500 species, suggesting that these animals could be present in the area even if not spotted by sightseers or that they could be introduced there for preservation purposes (e.g., Green iguana in fig.~\ref{fig:amazon_rainforest_net}). The latter hypotheses are obviously depending on the quantity and type of their connections —which give an idea of the quality of relations they would have with other present species— and would be more sensible by considering a full ecosystem framework, including as much species as possible and a reliable esteem of their local populations' size. Despite it might still be quite imprecise, this could allow sightseeing-recording platforms to test the absence of a specie from habitats identified as suitable to it by incentivizing data collection for that particular animal in those locations (e.g., through gamification).



