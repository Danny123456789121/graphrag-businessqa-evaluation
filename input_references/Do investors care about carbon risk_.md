# Do investors care about carbon risk?

# Patrick Bolton, Marcin Kacperczyk

PII: S0304-405X(21)00190-2

DOI: https://doi.org/10.1016/j.jfineco.2021.05.008

Reference: FINEC 3388

To appear in: Journal of Financial Economics

Received date: 21 October 2019

Revised date: 24 September 2020

Accepted date: 23 October 2020

Please cite this article as: Patrick Bolton, Marcin Kacperczyk, Do investors care about carbon risk?, Journal of Financial Economics (2021), doi: https://doi.org/10.1016/j.jfineco.2021.05.008

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2021 Published by Elsevier B.V.

# Do investors care about carbon risk?

# Patrick Bolton, Marcin Kacperczyk

# ABSTRACT

We study whether carbon emissions affect the cross-section of US stock returns. We find that stocks of firms with higher total carbon dioxide emissions (and changes in emissions) earn higher returns, controlling for size, book-to-market, and other return predictors. We cannot explain this carbon premium through differences in unexpected profitability or other known risk factors. We also find that institutional investors implement exclusionary screening based on direct emission intensity (the ratio of total emissions to sales) in a few salient industries. Overall, our results are consistent with an interpretation that investors are already demanding compensation for their exposure to carbon emission risk.

# JEL classification:

G12, G23, G30, D62

# Keywords

Carbon emissions, Climate change, Stock returns, Institutional investors

# 1. Introduction

Many studies seek to explain the cross-sectional pattern of stock returns based on exposures to aggregate risk factors such as size and book-to-market ratios, or firm-specific risk linked to observable firm characteristics. One variable that has so far been missing from the analysis is corporate carbon emissions. This omission may be for historical reasons, as concerns over global warming linked to carbon dioxide (CO2) emissions from human activity have only recently become salient. But, both the evidence

* We thank Jawad Addoum, Franklin Allen, Eric Bouyé, Kent Daniel, Charles Donovan, Elyse Douglas, Gerry Garvey, Lukasz Pomorski, Ailsa Roell, Zacharias Sautner, Gireesh Shrimali, Michela Verardo, Jeff Wurgler, and the referee for helpful suggestions. We also appreciate comments from seminar participants at Blackrock, EFA Conference, IESE, Newcastle University, the New Frontiers in Investment Research conference, NHH Bergen, NYU Law Roundtable on Climate Disclosure, UBS, University of Cardiff, and University College Dublin. We are grateful to Trucost for giving us access to their corporate carbon emissions data, and to Jingyu Zhang for very helpful research assistance. This project has received funding from the European Research Council (ERC) under the ERC Advanced Grant programme (grant agreement No. 885552 Investors and Climate Change).

Patrick Bolton: Columbia University, Imperial College London, CEPR, and NBER. Email: pb2208@columbia.edu.

Marcin Kacperczyk: Imperial College London and CEPR. Email: mkacperc@ic.ac.uk.

of rising temperatures and the renewed policy efforts to curb CO2 emissions raise the question of whether carbon emissions represent a material risk for investors that is reflected in the cross-section of stock returns and portfolio holdings.

Two major developments, in particular, suggest that this may be the case. First, the Paris COP 21 climate agreement of December 2015, with 195 signatories committing to limit global warming to well below 2°C above pre-industrial levels. Second, the rising engagement of the finance industry with climate change, largely as a result of the call to non-governmental actors to join the fight against climate change at the COP 21. Institutional investors are increasingly tracking the greenhouse gas emissions of listed firms and forming coalitions such as Climate Action 100+ to engage with companies to reduce their carbon emissions.1 More and more asset owners are following the lead of the Church of England Pension Fund, whose stated goal is “to demonstrate transparently that it has delivered on its commitment to be aligned to the Paris Agreement.”2

Even if the US has pulled out of the Paris Agreement under the Trump administration, and even if the commitments of the other remaining signatories are only partially credible, major curbs in CO2 emissions are likely to be introduced over the next decade. Primarily affected by these curbs are the companies with operations generating high CO2 emissions, or with activities linked to companies in the value chain that have high CO2 emissions. In light of these developments, one would expect to see the risk with respect to carbon emissions to be reflected in the cross-section of stock returns. Yet, considerable skepticism remains, not least in the US where the Trump administration had worked to upend regulations that limit CO2 emissions. For example, Darren Woods, ExxonMobil’s CEO, recently declared that “Individual companies setting targets and then selling assets to another company so that their portfolio has a different carbon intensity has not solved the problem for the world.” And that ExxonMobil was “taking steps to solve the problem for society as a whole and not try and get into a beauty competition.”3

The lack of consensus among institutional investors around climate change naturally raises the possibility that carbon risk may not yet be reflected in asset prices. To find out, in this paper we systematically explore whether investors demand a carbon risk premium by looking at how stock returns vary with CO2 emissions across firms and industries. We undertake a standard cross-sectional analysis, asking whether carbon emissions affect cross-sectional US stock returns.

There are several ways in which one might expect CO2 emissions to affect stock returns. First, since CO2 emissions are tied to fossil-fuel energy use, returns are affected by fossil-fuel energy prices and commodity price risk. Relatedly, firms with disproportionately high CO2 emissions may be exposed to carbon pricing risk and other regulatory interventions to limit emissions. The firms that are most reliant on fossil energy are also more exposed to technology risk from lower-cost renewable energy. Forward-looking investors may seek compensation for holding the stocks of disproportionately high CO2 emitters and the associated higher carbon risk they expose themselves to, giving rise to a positive relation in the cross-section between a firm’s own CO2 emissions and its stock returns. We refer to this as the carbon risk premium hypothesis.

An interesting question is whether carbon emissions are perceived to be a systematic risk factor and whether the carbon risk premium is tied to loadings on this risk factor. Carbon emissions could be a systematic risk factor if expected regulatory interventions to curb emissions apply uniformly to all emissions. For example, if a large federal carbon tax were to be introduced, this would be a systematic shock affecting all companies with significant emissions. Alternatively, most regulatory interventions could be introduced in a piecemeal way at the state, industry, and municipal level. Similarly, technological improvements in the use of renewable energy could be mostly targeted to particular operations or sectors. In this case, one would not expect carbon emissions to be a systematic risk factor.

1 See http://www.climateaction100.org/

2 Statement made by Adam Matthews, the fund’s director of ethics and engagement. The Church of England Pension Fund is co-chairing the IIGCC initiative.

3 Quoted in Exxon CEO Calls Rivals’ Climate Targets a ‘Beauty Competition’ by Kevin Crowley, Bloomberg News, March 5, 2020, https://www.bnnbloomberg.ca/exxon-ceo-calls-rivals-climate-targets-a-beauty-competition-1.1400957.

A second hypothesis is that financial markets are pricing carbon risk inefficiently and the risk associated with carbon emissions is underpriced. Carbon risk may not be fully integrated by most investors, who by force or habit look at future cash-flow projections through local thinking à la Gennaioli and Shleifer (2010), ignoring unrepresentative information about global warming and its attendant risks. To be sure, the cash-flow scenarios commonly used by financial analysts do not directly refer to carbon emissions and their possible future repricing. A recent study by In, Park, and Monk (2019) on a different sample than ours finds that a portfolio that is long stocks of companies with low carbon emissions and short stocks of companies with high emissions generates positive abnormal returns. We refer to this hypothesis as the market inefficiency, or carbon alpha, hypothesis. An important question we explore is whether financial markets underprice carbon risk (after controlling for other known risk factors, industry, and firm characteristics) to the point that responsible investors, who care about carbon emissions and climate change, could be “doing well by doing good.”

A third hypothesis is that the stocks of firms with high emissions are like other “sin stocks”; they are shunned by socially responsible, or ethical, investors to such an extent that the spurned firms present higher stock returns. A key question in this respect is how investors identify the firms to be divested from. Do they look at carbon emissions at the firm level, or do they pigeonhole firms into broader categories such as the industry they operate in? Even socially responsible investors that care about climate change may use sparse models (à la Gabaix, 2014) and not look much beyond industry categorizations, such as the energy and electric utility sectors, which produce a disproportionate share of CO2 emissions. Prominent divestors like the Rockefeller Brothers Fund, for example, who have pledged to divest from fossil fuel companies, largely focus on energy companies that extract coal and oil from tar sands. We refer to this as the divestment hypothesis.

A pioneer in producing company-level CO2 emissions data is the Carbon Disclosure Project (CDP). It has been joined by other leading providers of carbon data, including MSCI ESG Research and Trucost, among others. While more and more institutional investors make use of the data, it is not known how much individual companies’ stock returns are actually affected by the availability of these more granular CO2 emissions data to financial analysts. Our study relies on the Trucost EDX data, which cover around 1,000 listed companies since fiscal year 2005, and over 2,900 listed companies in the US since fiscal year 2016. We match these data with the FactSet returns and balance sheet data for all US-listed companies from 2005 to 2017.

Carbon emissions from a company’s operations and economic activity are typically grouped into three different categories: direct emissions from production (scope 1), indirect emissions from consumption of purchased electricity, heat, or steam (scope 2), and other indirect emissions from the production of purchased materials, product use, waste disposal, outsourced activities, etc. (scope 3). The scope 3 category in turn is separated into upstream and downstream indirect emissions. The data on scope 1 and scope 2 emissions are widely reported. Scope 3 emissions on the other hand are estimated using an input-output matrix. Although scope 3 emissions are the most important component of companies’ emissions in a number of industries (e.g., automobile manufacturing), they have not been reported by companies until recently.

Our main broad finding is that carbon emissions significantly affect stock returns. For all three categories of emissions, we find a positive and statistically significant effect on firms’ stock returns. We designate the higher returns associated with higher emissions as a carbon premium. We estimate how this carbon premium is related to three different measures of corporate emissions: 1) the total level of emissions; 2) the year-by-year change in emissions; and 3) emission intensity, which measures carbon emissions per unit of sales. A striking result is that the carbon premium is related to the level of (and to changes in) emissions, but not to emission intensity. One reason why the premium is tied to total emissions is that regulations limiting emissions are more likely to target activities where the level of emissions is highest. For example, in its planned climate stress test, the Bank of England focuses only on large firms and measures risk in terms of required reductions in the level of emissions.

4 See https://www.rbf.org/mission-aligned-investing/divestment.

5 See http://www.cdp.net/en-US/Pages/About-Us.aspx.

6 See https://www.msci.com/climate-change-solutions and https://www.trucost.com/policy-academic-research.

(see the 2021 biennial exploratory scenario on the financial risks from climate change (Bank of England discussion paper, 2019)). Similarly, since technological change generally involves a fixed cost, renewable energy is more likely to displace fossil fuels in firms where returns to scale are highest. Another consideration is that since emission intensity is a ratio, it is likely to be a noisier metric of carbon risk exposure. Two firms with identical emission intensities may vary substantially in their levels of emissions. Indeed, this is what we find: the correlation coefficient between the level of scope 1 emissions and emission intensity is 0.6, and significantly less for scope 2 and scope 3. Nevertheless, it is somewhat surprising that we find no premium associated with emission intensity since emission-intensive firms might well be the first to become unprofitable should the carbon price rise. Investors would then demand a premium for holding these firms.

Interestingly, there is also a significant carbon premium associated with the year-to-year growth in emissions. As one would expect, we find that the level of emissions is highly persistent. Hence, emission levels reflect a long-run risk exposure with respect to carbon emissions. Changes in emissions, in turn, reflect short-run effects; how much worse, or better, carbon risk gets. Of course, changes in emissions could also indicate changes in earnings, but we control for this effect by adding the company’s return on equity, sales growth, and earnings growth, among our independent variables.

The carbon premium is economically significant: A one-standard-deviation increase in respectively the level and change of scope 1 emissions leads to a 15-bps and 26-bps increase in stock returns, or respectively a 1.8% and 3.1% annualized increase. In addition, a one-standard-deviation increase in the level and change of scope 2 emissions leads to respectively a 24-bps and 18-bps increase in stock returns, or a 2.9% and 2.2% annualized increase. Finally, a corresponding one-standard-deviation increase in the level and change of scope 3 emissions increases stock returns by 33 bps and 31 bps per month, or 4.0% and 3.8% on an annual basis. Importantly, firms with higher emissions generate higher returns, after controlling for size, book-to-market, momentum, other well-recognized variables that predict returns, and firm characteristics, such as the value of property, plant & equipment (PPE), and investment over assets.

Other things equal, a carbon premium is the reflection of a lower investor demand for stocks of companies associated with high emissions. In equilibrium, this lower demand translates into a lower stock price, and possibly also lower holdings of high-emission stocks by some categories of investors. Following Hong and Kacperczyk (2009), we explore to what extent companies with high carbon emissions are treated like “sin stocks” by institutional investors. We find that, in aggregate, institutional investors do hold a significantly smaller fraction of companies with high scope 1 emission intensity, but they are not underweight companies with high levels of emissions. When we disaggregate by investor categories (mutual funds, insurance companies, banks, pension funds, and hedge funds), we find that insurance companies, pension funds, and mutual funds are underweight scope 1 emission intensity. The negative ownership effect of moving from high to low scope 1 emission-intensity firms is economically large and accounts for about 15%-20% of the cross-sectional variation in the ownership variable. This finding is in line with the rise in the sustainable investment movement and the popular negative exclusionary screening investment strategy followed by funds with an environmental, social, and governance (ESG) tilt.

We find that divestment is only based on scope 1 emission intensity. This is true both in aggregate and for each institutional investor category. Essentially, institutional investors have been applying exclusionary screens (or not) solely on the basis of scope 1 emission intensity. Even more remarkable, we find that when we exclude the industries with the highest CO2 emissions (oil & gas, utilities, and motor industries), there is no significant exclusionary screening at all by institutional investors. In other words, the exclusionary screening is done entirely in these salient industries; in all other industries, there is no significant divestment. Overall, these findings lead us to reject the divestment hypothesis. First, although there is significant divestment by institutional investors, it is not directly linked to an effect on stock returns. Institutional investor portfolios are significantly underweight firms with high scope 1 emission intensity, but stock returns are not affected significantly by emission intensity.

See Krueger, Sautner, and Starks (2020). Also, according to the Global Sustainable Investment Review 2018, negative/exclusionary screening is the largest sustainable investment strategy globally, representing $19.8 trillion of assets under management. http://www.gsi-alliance.org/wp-content/uploads/2019/03/GSIR_Review2018.3.28.pdf.

Our finding that stock returns are positively related to the level (and changes) of carbon emissions is largely consistent with the view that investors are pricing in a carbon risk premium at the firm level. This result contradicts the carbon alpha hypothesis, whereby investors holding a portfolio long stocks of companies with low carbon emissions and short stocks of companies with high emissions generates positive abnormal returns. Garvey, Iyer, and Nash (2018) and In, Park, and Monk (2019) suggest that portfolios that sort stocks by emission intensity (going long stocks with low intensity and short stocks with high intensity) generate a positive alpha. In contrast, we find that there is no significant effect of carbon intensity on stock returns. Our study differs in two important respects from theirs. First, we cover a different time period and sample of firms. Second, we control for industry, firm characteristics, and known risk factors, while neither of these studies includes all of these controls. Controlling for industry significantly affects the results. Also, in contrast to In, Park, and Monk (2019), we analyze the effects of carbon emissions for each scope category separately, thereby avoiding double counting.

Another important finding is that the carbon premium has only materialized recently. We show that if we look back to the 1990s by imputing the 2005 cross-sectional distribution of total emissions to the 1990s, there is no significant carbon premium, consistent with the view that investors at that time likely did not pay as much attention to carbon emissions. However, if we apply the same analysis to our sample period, by imputing the 2017 cross-sectional distribution of emissions back throughout our sample period, we find that there is a highly significant carbon premium.

To summarize, investors seem to take a somewhat schizophrenic attitude to carbon emissions. On the one hand, institutional investors clearly want to take a proactive approach by divesting from industries with high CO2 emissions. On the other hand, this categorical exclusionary screening approach only partially addresses the carbon risk issue. Indeed, investors price in a carbon emission risk premium at the firm level in all industries even though divestment is concentrated in the industries with the highest CO2 emissions (oil & gas, utilities, and transportation industries). If there is one general lesson that emerges from our analysis it is that carbon risk cannot just be reduced to a fossil fuel supply problem. It is also a demand problem. Once one factors in both the supply and demand aspects, all companies in all sectors are exposed to various degrees to carbon emissions risk. A coarse exclusionary approach focusing only on the energy and utility sectors misses the full extent of the problem investors face. Accounting for carbon risk is also required on the demand side, which inevitably involves the careful tracking of emissions at the firm level in all sectors.

Our study is related to a rapidly growing literature on climate change and financial markets. An early study by Matsumura, Prakash, and Vera‐Munoz (2014) of S&P 500 firms between 2006 and 2008 looks at the effects of direct carbon emissions on firm value, and the effects of voluntary public disclosure of emissions (through CDP) on firm value. They find that higher emissions are associated with lower firm values, but that voluntary disclosure mitigates the negative valuation effect of emissions. Relatedly, Chava (2014) looks at the effects of environmental concerns, as reflected in KLD ratings, on firms’ cost of capital. He finds that firms that derive substantial revenues from the sale of coal or oil, as reflected in a KLD rating, are associated with a higher implied cost of capital. In an extensive survey of institutional investors, Krueger, Sautner, and Starks (2020) also find that institutional investors believe that carbon emissions represent a material risk. Among their responses, institutional investors also say that they do not believe that there is substantial underpricing of carbon risk. Andersson, Bolton, and Samama (2016) propose a carbon risk hedging strategy for passive investors based on low carbon indexes.

More recently, Ilhan, Sautner, and Vilkov (2020) find that carbon emissions increase downside risk as reflected in out‐of‐the‐money put option prices. Hsu, Li, and Tsou (2019) look at the effects of environmental pollution on the cross-section of stock returns. They find that highly polluting firms are more exposed to environmental regulation risk and command higher average returns. Engle et al. (2020) construct an index of climate news through textual analysis of The Wall Street Journal and other media and show how a dynamic portfolio strategy can be implemented that hedges risk with respect to climate change news. Görgen et al. (2019) construct a carbon‐risk factor and estimate a carbon beta for firms. Monasterolo and De Angelis (2019) explore whether investors demand higher risk premia for carbon-intensive assets following the COP 21 agreement.

Other related studies explore the asset pricing consequences of greater material risks linked to climate events and global warming. Hong, Li, and Xu (2019) find that the rising drought risk caused by climate change is not efficiently priced by stock markets. Several studies examine climate change and real estate prices. Baldauf, Garlappi, and Yannelis (2020) find little evidence

of declining prices as a result of greater flood risk due to sea level rise. Bakkensen and Barrage (2017) find that climate risk beliefs in coastal areas are highly heterogeneous and that rising flood risk due to climate change is not fully reflected in coastal house prices. Bernstein, Gustafson, and Lewis (2019) find that coastal homes vulnerable to sea-level rise are priced at a 6.6% discount relative to similar homes at higher elevations. However, in a related study, Murfin and Spiegel (2020) find no evidence that sea level rise risk is reflected in residential real estate prices. Finally, Giglio et al. (2018) use real estate pricing data to infer long-run discount rates for valuing investments in climate change abatement.

The remainder of the paper is organized as follows. In Section 2, we describe the data and provide summary statistics. We discuss the results in Section 3. Concluding remarks are in Section 4.

# 2. Data and Sample

Our primary database covers the 2005-2017 period and is largely a result of matching two data sets by Trucost and FactSet in the US. Trucost provides information on corporate carbon and other greenhouse gas emissions. FactSet provides data on stock returns, corporate fundamentals, and institutional ownership. We performed the matching using ISIN as a main identifier. In some instances, in which ISIN was not available to create a perfect match, we relied on matching based on company names (after standardizing the company names in FactSet and Trucost we match the names with a similarity score of one). Finally, when there are multiple subsidiaries of a given company, we used the primary location as a matching entity. The ultimate matching produced 3,421 unique companies out of 3,481 companies available in Trucost. Among the 60 companies we were not able to match, more than half are not exchange listed and the remaining ones are small. Hence, we believe our data cover almost the entire universe of companies with available emission data.

# 2.1. Data on corporate carbon emissions

Firm-level carbon emissions data are assembled by seven main providers: CDP, Trucost, MSCI, Sustainalytics, Thomson Reuters, Bloomberg, and ISS. All these providers follow the Greenhouse Gas Protocol that sets the standards for measuring corporate emissions. More and more companies disclose their greenhouse gas emissions, and most large corporations report their emissions to CDP. Other providers rely on the CDP data and supplement it with other sources. Emissions can be measured directly at the source or more commonly by applying conversion factors to energy use. The Greenhouse Gas Protocol distinguishes between three different sources of emissions: scope 1 emissions, which cover direct emissions over one year from establishments that are owned or controlled by the company; these include all emissions from fossil fuel used in production. Scope 2 emissions come from the generation of purchased heat, steam, and electricity consumed by the company. Scope 3 emissions are caused by the operations and products of the company but occur from sources not owned or controlled by the company. These include emissions from the production of purchased materials, product use, waste disposal, and outsourced activities.

In some sectors, like automobile manufacturing, by far the most important component of their emissions is the aggregation of all their scope 3 emissions. The Greenhouse Gas Protocol distinguishes between 15 different categories of scope 3 emissions, including purchased goods and services, capital goods, upstream & downstream transportation and distribution, waste generated in operations, business travel, employee commuting, processing & use of sold products, and end-of-life treatment of sold products. According to CDP’s 2016 Climate Change Report, most scope 3 emissions are concentrated in two categories: purchased goods and services (around 44%) and use of sold products (around 48%). The Greenhouse Gas Protocol provides detailed guidance on how to identify a company’s most important sources of scope 3 emissions and how to calculate them.

See https://ghgprotocol.org.

See http://ghgprotocol.org/standards/scope-3-standard.

See CDP 2016 Climate Change Report “Tracking Progress on Corporate Climate Action.”

Purchased goods and services, this basically involves measuring inputs, or “activity data,” and applying emission factors to these purchased inputs that convert activity data into emissions data. The upstream scope 3 data from Trucost that we use is constructed using an input-output model that provides the fraction of expenditures from one sector across all other sectors of the economy. This model is extended to include sector-level emission factors, so that an upstream scope 3 emissions estimate can be determined from each firm’s expenditures across all sectors from which it obtains its inputs (see Trucost, 2019). Downstream scope 3 emissions caused using sold products can also be estimated and are increasingly reported by companies. Trucost has recently started assembling this data, but we were not able to include it in our study.

Because they are easier to measure, and because disclosure requirements are stricter, data on scope 1 and scope 2 have been more systematically reported and accurately estimated. As Busch et al. (2018) show, there is very little variation in the reported scope 1 and 2 emissions data across the data providers. Correlations in the reported scope 1 (scope 2) data average 0.99 (0.98), across the five providers CDP, Trucost, MSCI, Sustainalytics, and Thomson Reuters. However, when it comes to estimated scope 1 and scope 2 emissions (when reported data are missing), the correlations drop to 0.79 and 0.63, respectively for the three providers, Trucost, MSCI, and Sustainalytics, that offer these estimates. Finally, only two data providers, Trucost and ISS ESG, provide estimates of scope 3 emissions. The Trucost EDX database we use in our main analysis reports all three scopes of carbon emissions in units of tons of CO2 emitted in a year. We report the summary statistics of the emissions variables in Panel A of Table 1.

The average firm in our sample produces 1.97 million tons of scope 1 emissions, and is tied to 1.72 million tons of scope 3 emissions. The quantity of scope 2 emissions is relatively smaller, at 342,000 tons of CO2 equivalent. Notably, the median number is the largest for scope 3 emissions, as almost all companies in our sample are tied to a significant quantity of such emissions. The scope 1, 2, and 3 measures are in units of tons of CO2 and normalized using the natural log scale. We also report annual growth rates in each emission measure. To mitigate the impact of outliers, we winsorize all growth measures at the 2.5% level. The carbon intensity of a company is expressed as tons of CO2 equivalent divided by the company’s revenues in million US dollar units, also winsorized at the 2.5% level. The average (unwinsorized) scope 1 intensity in our sample equals 265.26 tons/million, while the intensities for scope 2 and scope 3 are 39.64 tons/million and 164.22 tons/million, respectively. The EDX database also provides information on whether the emissions data was reported or estimated, which allows us to do a sensitivity analysis and determine how the results are affected by the exclusion of the estimated data. We describe how the data breaks down into firms with reported and estimated emissions data in Table 2. As Matsumura, Prakash, and Vera‐Munoz (2014) note, firms that do not report their emissions are typically smaller (and therefore have smaller emissions) and are less profitable. But in other respects, firms that report their emissions have similar characteristics to those that do not. In particular, their stock returns, volatility, leverage, book-to-market ratios, capital expenditures, and betas are very similar.

We also report alternative measures Trucost provides, in particular: i) CARBON DIRECT, which adds three additional greenhouse gases to the GHG Protocol scope 1 measures; ii) CARBON INDIRECT, which covers a slightly broader set of emissions by the direct suppliers to a company than scope 2; iii) GHG DIRECT, measured in US dollars, which covers all direct external environmental impacts of a company. Trucost applies a monetary value to GHG emissions quantities, which represents the global average damage of each environmental impact; and iv) GHG INDIRECT, which covers indirect supply chain environmental impacts. These are estimated impacts based on Trucost’s environmental impact models. Again, these are reported in US dollars and represent the global average damages of each environmental impact.

How correlated are these different emission variables? We report the cross-correlations in Panel A of Table 3. As one would expect, the levels of all three categories of emissions are positively correlated. Yet, the coefficients are relatively small. Similarly, the level of scope 1 emissions is obviously positively correlated with scope 1 emission intensity, but the size of the coefficient is only 0.6, reflecting the fact that two firms with the same scope 1 intensity may have very different levels of emissions.

More than 6,300 companies worldwide answered CDP’s climate change questionnaire in 2018. Of these, 76% disclosed scope 1 emissions, 68% scope 2 emissions, and 38% scope 3 emissions (see https://www.cdp.net).

# 2.2. Variables in cross-sectional return regressions

A large firm, with high emissions, can have the same emission intensity as a small firm. The low correlation between levels and intensity is even more pronounced for scope 2 (0.24) and scope 3 (0.27). In Panel B, we also report the autocorrelation coefficients for the different measures of emissions. Emission levels for all three categories are highly persistent, with an autocorrelation coefficient of 0.977 for scope 1, 0.955 for scope 2, and 0.967 for scope 3. Interestingly, the year-to-year growth in emissions also has some persistence, especially for scope 3 emissions. As for the emission intensity variables they are, not surprisingly, also highly persistent as sales are highly persistent.

We also analyze the average values of all three emission sources over time. Fig. 1 and Table 4 present the results. As one might expect, there is a steady decline in scope 1 and scope 3 emissions at the firm level over time as a result of energy efficiency improvements, technological innovations, and an increase in the reliance on renewable energy sources. There is a sharp decline in scope 1 emissions from 2015 to 2016. However, this mainly reflects the addition by Trucost of many smaller firms to the sample in 2015, as can be seen in Fig. 2. The addition of all these firms to the sample also explains why total scope 3 emissions sharply increase from 2015 to 2016, and why total scope 1 emissions remain flat even though per-firm emissions decline. All these results are further confirmed by the numbers in Panels A and B of Table 4; averages for all firms in our sample are in Panel A while those conditioned on the presence in the sample prior to 2015 are in Panel B. We can see that when we drop the new firms added in 2016 from the sample, the averages for 2016 and 2017 are very close to the numbers in 2015. While we still observe some decline in scope 1 emissions, there is no such decline in scope 2 and scope 3 emissions. If anything, the numbers for scope 3 emissions go up, although not by much.

We note that firms with significant emissions are represented in a wide range of industries. In Table 5, we present the distribution of firms in our sample with respect to the six-digit Global Industry Classification (GIC 6). Banks, biotech, and oil & gas are the most represented industries, with each one having more than 150 firms.12 In Table 6, we provide a list of industries with the highest and the lowest intensity of emissions. Power, electric, and multi-utility industries produce the most scope 1 emissions, while consumer finance, thrifts and mortgages, and capital markets are the cleanest. The ranking is somewhat different when we classify industries with respect to their scope 2 and scope 3 emissions. Metals and mining, electric utilities, and construction materials are the three most scope 2 emission-intensive industries (the cleanest industries mimic those based on scope 1 classification). In turn, food products, metals and mining, and construction materials are the three most scope 3 emission-intensive industries. Internet software and services, health care technologies, and software are the three least emission-intensive industries. The Trucost industry classification is finer than the GIC six-digit classification. Given that we control for industry a natural question is how sensitive the results are to the classification itself. The classification in theory could be so fine that it includes only one firm in each industry or so coarse that it includes all firms in one industry. Adding industry fixed effects would be meaningless under these polar classification systems. As a robustness check, we also perform our analysis under the GIC classification and report the results in Table A.4 in the Appendix.

Finally, we observe not only substantial variation in the growth rates of emissions across different industries, but also significant variation in the rates of all three categories of emissions across firms within the same industry. Fig. 3 displays the time series plots of the average cross-sectional standard deviations of emission growth rates across all firms (Panel A) and across all firms within a given GIC 6 industry (Panel B). Even though the scale of the variation in Panel A is larger than that in Panel B, there is still a significant dispersion in emissions in Panel B. Moreover, the standard deviation in carbon emission growth rates is very stable over time. In particular, the standard deviation did not significantly change following the addition of new firms to the sample in 2015.

12 Some firms in this table are classified into multiple industries; hence, the total number of firms in the table (3917) exceeds the number of unique firms in our sample (3421).

Our empirical analysis of stock returns employs a monthly measure of returns as a dependent variable. In our cross-sectional return regressions, the dependent variable RETi,t is the monthly return of an individual stock i in month t. Our return data primarily comes from FactSet, but for a small subset of delisted firms, we replace the return data with delisting-adjusted values from Compustat. Finally, we remove observations with returns greater than 100% to mitigate the impact of outliers. The number of excluded firm/month observations is 109 and its exclusion does not materially affect our results. However, using unrestricted returns data would be problematic as the data, for example, include four observations with monthly returns greater than 10,000%.

Our control variables are defined as follows: LOGSIZEi,t is the natural logarithm of firm i’s market capitalization (price times shares outstanding) at the end of year t; B/Mi,t is firm i’s book value divided by its market capitalization at the end of year t; LEVERAGE is the book leverage of the company; ROEi,t is the firm’s earnings performance, given by the ratio of firm i’s net yearly income divided by the value of its equity; MOMi,t is the average of the most recent 12 months’ returns on stock i, leading up to and including month t-1; INVEST/A represents the firm’s capital expenditures divided by the book value of its assets; HHI is the Herfindahl concentration index of firms with respect to different business segments, based on each segment’s revenues; LOGPPE is the natural logarithm of the firm’s property, plant, and equipment; BETAi,t is the market beta of firm i in year t, calculated over the one year period using daily data; VOLATi,t is the standard deviation of returns based on the past 12 months of monthly returns; SALESGRi,t is the dollar change in annual firm revenues normalized by last month’s market capitalization; EPSGRi,t is the dollar change in annual earnings per share, normalized by the firm’s equity price. To eliminate the impact of outliers, we winsorize B/M, LEVERAGE, and INVEST/A at the 2.5% level, and MOM, VOLAT, SALESGR, and EPSGR at the 0.5% level. We report the summary statistics of these variables in Panel B of Table 1.

The average firm’s monthly stock return is 1.14%, with a standard deviation of 10.84%. The average firm has a market capitalization of $13 billion, with a median value of $3.8 billion. The average book-to-market ratio is 0.50, while the average book leverage is 24%. The average market beta is 1.10, slightly more than that of the market.

# 2.3. Variables in the time series return regressions

The variables for our time series regressions are defined as follows: MKTRFt is the monthly return of the CRSP value-weighted portfolio in month t, net of the risk-free rate; SMB, HML, MOM, and CMAt are well-known portfolio return series downloaded from Ken French’s website: SMB is the monthly return of a portfolio that is long on small stocks and short on large stocks; HML is the monthly return of a portfolio that is long on high book-to-market stocks and short on low book-to-market stocks; MOM is the monthly return of a portfolio that is long on past one-year return winners and short on past one-year return losers; CMA is the monthly return of a portfolio that is long on conservative investment stocks and short on aggressive investment stocks. BAB is the monthly return of a portfolio that is long on low-beta stocks and short on high-beta stocks; LIQ is the liquidity factor of Pastor and Stambaugh; NET ISSUANCE is the monthly return of a portfolio that is long on high-net-issuance stocks and short on low-net-issuance stocks. Net issuance for year t is the change in the natural log of split-adjusted shares outstanding from the fiscal yearend in t-2 to the fiscal yearend in t-1; IDIO VOL is the monthly return of a portfolio that is long on low idiosyncratic volatility stocks and short on high idiosyncratic volatility stocks. We present the summary statistics for the various portfolio returns in Panel C of Table 1.

The average market risk premium in our sample is 0.7% per month. Other factors with relatively high risk premia are net issuance and BAB. Somewhat atypically, the value factor return in our sample is equal to 0%. Similarly, the momentum factor generates a mere 0.07% per month, and the volatility factor has a negative return of -0.18% per month.

# 2.4. Variables in divestment regressions

Our institutional ownership regression variables are: IOi,t, which is the fraction of the shares of company i held by institutions in the FactSet database at the end of year t. IO is calculated by aggregating the shares held by all types of institutions.

at the end of the year, and then dividing this value by the number of shares outstanding at the end of the year. We further decompose the institutional ownership with respect to subgroups of owners. IO_BANKS is the ownership by banks; IO_INSURANCE is the ownership by insurance companies; IO_INVESTCOS is the ownership by investment companies (e.g., mutual funds); IO_ADVISERS is the ownership by independent investment advisers; IO_PENSIONS is the ownership by pension funds and IO_HFS is the ownership by hedge funds. Even though the total institutional ownership captures the intensive margin only, the range of disaggregated ownership variables varies from 0% to 100% (as long as the total institutional ownership in the data has a positive value).

The control variables in the ownership regressions include PRINVi,t, which is the inverse of firm i’s share price at the end of year t; VOLATi,t is the standard deviation of monthly stock returns for firm i over the one-year period; VOLUMEi,t is the average daily trading volume (in $million) of stock i over the calendar year t. NASDAQi,t is an indicator variable equal to one if a stock i is listed on NASDAQ in year t, and zero otherwise; SP500i,t is an indicator variable equal to one if a stock i is part of the S&P 500 Index in year t, and zero otherwise. We report the summary statistics for these variables in Panel D of Table 1.

The average IO is 0.77, and the cross-sectional standard deviation of IO is 0.22. In other words, in a typical year, a typical firm has about 77% of its shares held by institutional investors, and the standard deviation of institutional ownership in a typical cross-section is 22%. Among the different institutional owners, independent advisers are the biggest holders, with an average stock’s ownership equal to 43.9%, followed by investment companies with an average 18.2% ownership. Banks and insurance companies, in turn, are the smallest institutional owners. The average daily stock return volatility in our sample is 10% or annualized 158.7%. The average daily stock volume is $440,000. Finally, about 30% of stock-month observations are companies listed on NASDAQ, and 37% observations are firms from the S&P 500 Index.

# 3. Results

We begin our analysis by investigating the determinants of scope 1, scope 2, and scope 3 emissions. We then turn to the evaluation of the carbon return premium in the cross-section of stocks. We next explore the time-series properties of the cross-sectional carbon premium with respect to well-known risk factors. Finally, we consider the divestment hypothesis by looking at institutional ownership patterns.

# 3.1. Determinants of carbon emissions

Since emissions are not reported by all companies, one basic issue to explore first is how companies that do report their emissions compare with non-reporting companies. To assess the quantitative differences on the extensive margin, we compare various firm-level characteristics for the reporting and non-reporting firms. We describe basic summary statistics of the two categories of firms in Table A.1 of the Appendix. As one might expect, we find that larger firms are more likely to report their emissions. Also, firms with lower book-to-market ratios and higher book leverage are more likely to report emissions. At the same time, the two groups of firms do not differ significantly in terms of their stock returns or investment levels.

Next, we assess the differences in emission levels, year-by-year changes, and emission intensities across firms using a regression framework. Our dependent variables are levels, changes, and intensities of scope 1, scope 2, and scope 3. Since there is little theory that can guide us on what determines the level of carbon emissions, especially with regard to their different sources, we include a host of firm-level variables, comprising LOGSIZE, B/M, ROE, LEVERAGE, INVEST/A, HHI, LOGPPE, SALESGR, and EPSGR. To reflect the possibility that firm-level emissions could concentrate across firms and over time, we cluster standard errors at the firm and year levels. Standard errors in all panel regressions become significantly smaller in alternative specifications that cluster at the firm, industry, time, or industry and time levels. We present the results in Table 7.

Not surprisingly, all three categories of emission levels, and changes in emissions, are significantly positively related to LOGSIZE. However, scope 1 and scope 3 emission intensities are weakly negatively related to LOGSIZE. The level of emissions is also significantly associated with high book-to-market ratios, high tangible capital (PPE), highly levered firms, and firms with high

# 3.2. Evidence on cross-sectional returns

For all three categories of emissions, we relate in turn the level of companies’ emissions, the year-to-year growth in emissions, and the companies’ emission intensity to their corresponding stock returns in the cross-section. We first estimate the following cross-sectional regression model using pooled OLS:

(1) where measures the stock return of company i in month t and Emissions is a generic term alternately standing for SCOPE 1, SCOPE 2, and SCOPE 3 emissions. The vector of controls includes a host of firm-specific variables known to predict returns, such as LOGSIZE, B/M, ROE, LEVERAGE, MOM, INVEST/A, HHI, LOGPPE, BETA, VOLAT, SALESGR, and EPSGR. We also include year/month fixed effects. We cluster standard errors at the firm and year levels. Our coefficient of interest is.

We report the results in Table 8, Panel A. Column 1 shows the results for SCOPE 1; column 2 for SCOPE 2, and column 3 for SCOPE 3. For all three categories of emissions, we find a positive and statistically significant effect on firms’ stock returns. The effect is also economically significant: a one-standard-deviation increase in SCOPE 1 leads to a 13-bps increase in stock returns, or 1.5% annualized, and a one-standard-deviation increase in SCOPE 2 leads to a 23-bps increase in stock returns, or 2.8% annualized. Finally, a one-standard-deviation increase in SCOPE 3 increases stock returns by 30 bps per month, or 3.6% annualized.

Since emissions tend to cluster significantly within specific industries, a question of interest is whether the firm-specific differences can be attributed to industry-specific effects. To examine this possibility, we additionally include industry-fixed effects using the Trucost industry classification. The results presented in columns 4 to 6 are quite striking. Including industry effects significantly strengthens the cross-sectional dispersion of returns due to carbon emissions. In fact, the economic significance increases by anywhere between 70% and 280% relative to the model without industry effects.

We also plot the time series of the cumulative values of the unadjusted and industry-adjusted carbon premia in Fig. 4. Because different emission variables have different supports, we express the magnitudes in terms of unit standard deviation of each variable at each cross-section in time, so that all plots of the cumulative effect show comparable numbers in terms of economic significance. As can be seen in the figure, there are large positive cumulative returns for all measures of total emissions. The economic magnitudes of the effect become even larger once we factor in differences in industry exposures.

We next estimate the same cross-sectional regression model (1) replacing the level of emissions (LOG (Emissions TOT)) with the year-to-year growth in emissions (Δ(Emissions)). The results are reported in Table 8, Panel B. We find again a positive and statistically significant effect of the growth in emissions on stock returns. Interestingly, controlling for industry makes almost no difference when it comes to the effect of the growth in emissions. To allay any concern that our results may be driven by the correlation between emissions and size, we provide additional robustness tests in which we estimate univariate regression models with respective emission variables only, and regressions with emissions and size only. The results, reported in Table A.2 of the Online Appendix indicate that size is an important control when one considers the level of total emissions as a regressor but it is not as important in the model with the growth rate of emissions. Note also that ROE has a significant positive effect on stock returns under this specification (it is insignificant in the specification with emission levels). We attribute this to the fact that firms HHI, SALESGR, and EPSGR are measured as of time t to reflect the fact that all three may have a nontrivial contemporaneous effect on the level of emissions at time t.

with high emission growth likely also have higher earnings, which could result in higher stock returns (to the extent that the higher earnings outcome is unanticipated).

We also plot the time series of the cumulative values of the unadjusted and industry-adjusted carbon premia related to the growth in emissions in Fig. 5. All measures of emissions exhibit a steady rate of increase in the carbon premium over time.

Finally, we estimate the cross-sectional regression model in (1) for emission intensities. We report the results in Table 8, Panel C. There is no significant effect of emission intensity on returns for any of the three categories of emissions, whether we control for industry or not. The cumulative effect of emission intensity on the carbon premium, presented in Fig. 6, is also quite weak, with the exception of scope 2 for which we observe a slightly positive trend. Overall, these results reveal that there is a significant carbon premium with respect to the level of emissions, reflecting firms’ long-run risk exposure to carbon emissions, and a premium with respect to the growth in emissions, which capture the more short-term evolution of firms’ risk exposure to future emissions.

One open question with our analysis above is that we use carbon emission data in year t to explain monthly returns over the same year t. This could conceivably introduce a look-ahead bias. That is, under this specification we might unwittingly relate stock returns for some months in year t to emission data that might not yet have been available to investors. To address this question, we undertake the following robustness check. We relate monthly stock returns with a lag of respectively 0 to 12 months between the time when emissions are reported and the month when returns are realized.

Another interpretation of the results with lagged returns is that investors have limited attention and do not immediately absorb new information about carbon emissions at the firm level (Kacperczyk, Van Nieuwerburgh, and Veldkamp, 2016). In that case, carbon emissions for year t will be gradually reflected in returns over the year. An additional consideration is that investors obtain information about carbon emissions from multiple sources that are not all available at the same time. For example, a lot of firms disclose their emissions first to the CDP, data which then is merged into and combined with other sources by Trucost. Different information that is likely to be highly correlated with other information (given that all providers use the same data collection protocols) becomes available at different times. This is another reason why carbon emissions are only gradually reflected in stock returns.

We report the results in Table A.3. A remarkable pattern emerges from this analysis. Panel A1 reports the results for LOG (SCOPE 1 TOT). The coefficient is statistically significant for the first month (without industry fixed effects), remains significant at the 5% level until month 6 (with industry fixed effects), and is insignificant thereafter. Not surprisingly, it takes time for information about emissions to be reflected in stock prices, but eventually (after six months or so) this information appears to be fully absorbed. Essentially the same pattern is observed for the level of scope 2 and scope 3 emissions (with a somewhat faster (slower) integration of scope 2 (scope 3) emission information into stock prices), as the results in Panels A2 and A3 show. The same pattern is present for the growth in total emissions, as can be seen in panels B1, B2, and B3. However, emission intensity is nearly always insignificant, as we report in Panels C1, C2, and C3. The only visible exception is scope 1 emission intensity, which is significant at the 5% level in month 6 in the model with industry fixed effects. We conclude from this analysis that our results are not biased by a look-ahead effect.

Another possible explanation is that firms with higher emissions have also been exposed to unexpected positive value shocks. We explore this hypothesis by analyzing returns that strip out the effect of earnings surprises. Specifically, we subtract from the monthly stock returns the component that is realized on earnings announcement days and re-estimate the regression model in (1) with the adjusted returns. We report the results in Table 9 for the level of total emissions (Panel A), for the growth rate of emissions (Panel B), and for emission intensity (Panel C). We find no significant differential effect of earnings announcements on the carbon premium. Stocks with higher levels and growth rates of emissions still have higher returns, and emission intensity is still insignificant.

# 3.3. Carbon premium and risk factors

# Is the carbon premium linked to traditional risk factors?

To answer this question, we estimate the following time-series regression model using monthly data:

, (2)

where is the carbon return premium estimated from the cross-sectional Fama-MacBeth regression in Eq. (1); F is a set of factor-mimicking portfolios that includes MKTRF, HML, SMB, MOM, CMA, BAB, LIQ, NET ISSUANCE, and IDIO VOL. These factors have been widely used in many studies of asset prices. There are also economic reasons to believe that they could be meaningfully related to our carbon factor. Specifically, the first five factors correspond to the classic framework of Fama and French. In light of our results reported above, firm-level emissions are related to firm size and to firms’ growth opportunities; hence we include both the SMB and HML factors. The investment factor, CMA, controls for any differences in investments across firms. The market and momentum factors are standard controls in all time-series regressions. The BAB factor controls for the possibility that high carbon risk firms may be exposed to margin investments. The liquidity factor controls for possible differences in market liquidity among firms with different levels of carbon emissions, which could arise if some firms are not as actively traded as others due to ESG norm-based reasons. The net-issuance factor controls for any variation in capital structure and market timing by firm managers. Finally, the idiosyncratic volatility factor controls for the possibility that the measure of risk we capture may be idiosyncratic in nature. We calculate the standard errors of the coefficients using the Newey-West procedure with 12 lags to account for autocorrelation in error terms. Our coefficient of interest is , which measures the residual carbon premium, controlling for other risk/style factors.

# Panel A

Panel A in Table 10 shows the results for the carbon premium related to total emissions. In the odd columns, we report the unconditional carbon premium as a benchmark. In the even columns, we report results from regressions that add various factors MKTRF, HML, SMB, MOM, CMA, BAB, LIQ, NET ISSUANCE, and IDIO VOL. Comparing the odd and even columns for the respective scope categories of emissions, we find that the carbon premium remains statistically and economically significant after we adjust for differential factor exposures. However, the economic size of the premium is about 10%-20% smaller in magnitude. Overall, the regression intercepts from the cross-sectional return regressions are both economically and statistically significant in the presence of various risk factors.

# Panel B

Panel B shows the results for the carbon premium related to the growth rate in total emissions. We find again that the set of standard risk factors cannot explain the average value of the carbon premium for any of the emissions categories. This time, however, the difference in magnitudes across specifications is much smaller.

# Panel C

Panel C gives the results for emission intensity. Whether unconditionally or conditionally on the risk factors, we find no significant carbon premium.

Overall, our time-series regression results show that the carbon premium cannot be explained by known risk factors. This result reinforces the finding in Section 3.2 that the level of carbon emissions contains independent information about the cross-section of average returns.

# 3.4. The divestment hypothesis

An important possible explanation for the observed carbon premium could be under-diversification resulting from divestment and exclusionary screening of stocks with high carbon emissions by institutional investors implementing a sustainable investment policy. To the extent that some investors may shun companies with high carbon emissions, risk sharing would be limited, and idiosyncratic risk could be priced (e.g., Merton, 1987; Hong and Kacperczyk, 2009). If the extent of such divestment is high, one would expect to see significant pricing effects.

We test this possibility by looking at the portfolio holdings of institutional investors. Formally, we estimate the following pooled regression model:

. (3)

13

We consider ownership effects based on carbon intensity, the measure that is most aligned with explicit mandates imposed by socially sensitive asset managers. In the Online Appendix, Table A.4, we also present the results for the less commonly used measures of total emissions and growth in emissions. As these results confirm, these variables have no significant impact on institutional investor portfolios. The vector of controls includes LOGSIZE, PRINV, B/M, MOM, BETA, VOLAT, VOLUME, NASDAQ, and SP500. All regressions include year/month fixed effects. Also, carbon emissions tend to vary geographically, due to resource-driven firm locations. It is thus possible that the geographic location may also interact with ownership incentives. We test this idea by including in the ownership regression state fixed effects determined by the firm headquarters’ locations (in even columns). Our coefficient of interest is [missing value], which measures the degree of avoidance of firms with greater carbon emissions. We cluster standard errors at the industry and year levels.

# 3.5. Coarse Categorization

In Panel A of Table 11, we report the results for the aggregate institutional ownership measure. Columns 1 and 2 show the results for SCOPE 1 INT, respectively without and with state fixed effects. Both coefficients are negative and statistically significant at the 5% level. The economic effect of the divestment is relatively modest: a one-standard-deviation increase in SCOPE 1 leads to approximately a 1.3-percentage-point decrease in aggregate institutional ownership, which is about 6.3% of the cross-sectional standard deviation in ownership. In contrast, the coefficients are statistically insignificant for SCOPE 2 INT and SCOPE 3 INT, indicating that the exclusionary screens institutional investors apply in constructing their portfolios are entirely based on SCOPE 1 INT.

The institutional investor world pools a number of different constituencies with possibly different investor pressures. We conjecture that certain institutions, such as insurance companies, investment advisers, or pension funds, are more likely to face investor pressure, and thus they avoid high-emission companies, as opposed to mutual funds and hedge funds who are natural arbitrageurs. We test this hypothesis formally by dividing the institutional investors’ universe into six categories: banks, insurance companies, investment companies, independent advisers, pension funds, and hedge funds. For each category, we obtain their stock-level institutional ownership and estimate the regression model in (3) for each of them separately. Panel B reports the results broken down by investor category. We observe a strong cross-sectional variation in the ownership patterns. Insurance companies, investment advisers, and pension funds tend to hold less of the high scope 1 emission companies. At the same time, we observe positive, though weaker, ownership effects for banks, investment companies, and hedge funds, consistent with these groups being natural arbitrageurs. The divestment effects are economically large. A movement in SCOPE 1 INT from one standard deviation below the mean to one standard deviation above the mean, corresponding to a spread between low and high-emission firms leads to a reduction in ownership by 21%, 5%, and 4% of the cross-sectional standard deviation of ownership for investment advisers, insurance companies, and pension funds, respectively. In particular, given its large aggregate shares of stock holdings, the effect through investment advisers could lead to significant pricing effects. In sharp contrast to the results for SCOPE 1 INT, we observe that (with the exception of banks loading up positively on SCOPE 3 INT) all coefficients for the different investor types are small and statistically insignificant, which suggests that institutional investors do not seem to discriminate between stocks with regard to their scope 2 and scope 3 emission intensities.

Overall, institutional investors do significantly divest from firms associated with high SCOPE 1 INT. They do not screen companies based on the level of their emissions (or growth in emissions), even though the carbon premium is associated with these variables. They prefer to screen firms based on how efficiently they use fossil fuel energy and do not seem to be concerned about reducing their exposure to the level of carbon emissions per se. We conclude from these findings that, unlike for “sin” stocks (as shown by Hong and Kacperczyk, 2009), limited risk sharing caused by divestment cannot alone explain why we observe a return premium for companies with higher levels (and growth) of emissions.

It is often pointed out that only a handful of industries produce the most significant fraction of carbon emissions.14 The typical salient industries that are mentioned are oil & gas (GIC = 2), utilities (GIC = 65-69), and transportation (GIC = 19, 20, and 23). It is therefore natural to wonder whether our results are disproportionately driven by these sectors, and whether our cross-sectional carbon premium would become significantly smaller if we exclude these industries from our analysis.

In Table 12, we report the results for the subset of firms, excluding the sectors mentioned above. Panel A reports the results for total emissions, Panel B for the growth rate in emissions, and Panel C for emission intensity. Compared with the results in Table 8, we observe that, if anything, excluding these salient sectors strengthens the results on the firm-level carbon premium. These findings imply that there is a coarser categorization of companies by investors within the salient industries, where returns are less sensitive to differences in emissions across firms.

In Table 13, we report the results on institutional ownership when the salient high-CO2 industries are excluded. Consistent with Gabaix (2014), we find that coarse industry-level categorization drives our divestment results. Indeed, there is no significant divestment in the other industries. This is true in the aggregate as well as for the different categories of investors. It is as if investors decided to reduce their exposure to certain industries by divesting from some firms but holding on to the best in class in terms of scope 1 emission intensity in those industries. In Table A.5 of the Online Appendix, we provide additional evidence on this result with respect to levels and changes in emissions. We do not observe any divestment based on levels of emissions, but some divestment based on the growth of scope 2 and scope 3 emissions. This divestment is particularly strong for pension funds.

# 3.6. Investor awareness

The carbon premium in stock returns could also be affected by the changing awareness of investors about carbon risk. In particular, one would expect that periods with greater climate change awareness would have a higher carbon premium. We evaluate this hypothesis in two ways. First, we compare the estimated carbon premium before and after the Paris Agreement in 2015. Second, we impute carbon emissions in the 1990s based on their levels in 2005 and estimate the carbon premium over this decade and compare this premium to the one obtained over our sample period, when similarly imputing back carbon emissions based on the levels of emissions in 2017. Both tests offer complementary views on the role of changing investors’ attention. The first test allows us to assess the short-term impact of changing attention, while the second test is more suited for the long-term changes in attention.

The Paris Agreement possibly raised both the awareness of risks tied to carbon emissions and the prospect of regulatory interventions to limit carbon emissions. One could therefore expect that the carbon risk premium would increase after 2015 following the Paris Agreement. We test this hypothesis by estimating the regression model in (1) on the two sub-periods: 2005-2015, and 2016-2017.15 We report the results in Table 14. We find that indeed the premium associated with all three categories of emissions is larger during the 2016-2017 subperiod, especially for scope 1 and scope 2. This could be seen as evidence that investors care more about carbon risk following the Paris Agreement. However, an important caveat is that our sample increases after 2015, so that the difference in returns pre and post Paris could be attributed to the new firms that were added to our sample. We explore this possibility in the Online Appendix and indeed find in Table A.6 that the increase in return premium is mostly due to the addition of the new firms. We find that when we exclude the new firms, the carbon premium becomes insignificant in the two years following the Paris Agreement. The insignificance of the carbon premium does not necessarily mean that carbon risk is no longer priced after the Paris Agreement in 2015; it could be due to a weak statistical power given how noisy returns tend to be.

14 For instance, in a 2016 report, the International Energy Agency estimates that 39% of CO2 emissions come from electricity and heat production, 30% from transport, and 11% from industrial production (see https://www.iea.org/media/statistics/Energy_and_CO2_Emissions_in_the_OECD.pdf).

15 To enhance the statistical robustness of our results, we now cluster standard errors at the firm and year-month levels.

We further explore the cross-sectional variation of the effect of the Paris Agreement by examining whether the awareness that the Paris Agreement raised had a differential effect on the returns of firms with different exposures to carbon policy risk. We measure the exposures using our three measures of firm-level emissions. Our treatment sample is the subset of firms in the largest quartile of the distribution of firms sorted by the size of their carbon emission as of the end of 2014. We match these firms with a control group of firms with similar characteristics identified by two different techniques: the nearest neighbor and the Mahalanobis distance. The matching characteristics we use are the same as those we include in our return regressions. We report the results based on the nearest neighbor matching in Table 15. The results based on Mahalanobis matching are qualitatively similar.

To validate the quality of our matching, in Table A.7, we show, as an example, the balance test for the matched samples of treatment and control firms based on the scope 1 emission levels. We find that the two samples are not very different from each other along many firm-level dimensions. Notable exceptions are market capitalization, book-to-market ratio, return on equity, and property plant and equipment for which the differences are statistically significant, though not economically large. Importantly, the differences in market capitalization and PPE are expected given that the treatment sample is based on the size of firm emissions, which are strongly correlated with both characteristics. Next, we compare the returns of firms in the treatment and control groups in the one-year period around the Paris Agreement of December 2015. Formally, we estimate the following difference-in-differences regression model:

where TREAT is a generic indicator variable taking the value one for firms in the treatment sample and zero for firms in the control sample, and AFTER is an indicator variable equal to zero for the period 2015/05-2015/11 and equal to one for the period 2015/12-2016/05. We also include firm and year-month fixed effects in the regression. We estimate this model separately for each scope and emission measure. In the regressions, the sorts correspond to each scope measure, which then separately identify each individual treatment variable. Our coefficient of interest is e1, which measures the differential effect of the change on firms with high emissions and firms with low emissions.

In Panel A of Table A.7, we present the results for the level of total emissions. We find a strong and positive effect on returns based on scope 1 emissions, but no significant effects for the other two scopes of emissions. The effect is economically large, implying that the Paris Agreement resulted in an average increase in returns of more than 10.6% over the six-month period. In Panel B, we show the results based on changes in emissions. While the magnitudes of the results for scope 1 and scope 3 based on the model with industry fixed effects are fairly large (between 3.7% and 4.5%), they are statistically insignificant. In Panel C, we present the results based on carbon intensity. Surprisingly, we find a strong negative coefficient for scope 3 emissions. The effects for the other two scopes are small and insignificant. Overall, these results on the differential cross-sectional effects of the Paris Agreement are broadly consistent with our other results but their statistical significance is relatively small. Again, one of the reasons could be the relatively small statistical power of the tests, as returns are generally quite noisy. Another reason could be that the salient effects, such as Paris Agreement, take a longer time to materialize in investors’ beliefs.

To offer a longer-term perspective on the changing investors’ beliefs, we exploit the fact that climate change and carbon emissions were not yet salient issues in the 1990s. It is only in the last two decades, with the accumulation of CO2 in the atmosphere and the repeated record-breaking temperatures, that climate change has turned into a widespread concern. This naturally raises the question of whether stock returns were already affected by corporate carbon emissions in the 1990s. If information about firm-level emissions was scarce and/or investors did not pay attention to carbon risk, one would expect that the pricing effects we identify between 2005 and 2017 would be much smaller back then. Given that our carbon emissions data begins in 2005, we cannot evaluate this hypothesis directly. However, we can impute back the unobserved emissions data for each firm in the 1990s from the values we observe later on. In other words, since emission levels are highly autocorrelated and the cross-sectional variation in emissions is stable over time (see Fig. 3), it seems reasonable, as a first pass, to assume that the cross-sectional variation of emissions in the 1990s tracks closely that observed in our data.

Specifically, we make the assumption that each firm with stocks trading during the 1990s has an emission intensity equal to the first officially reported value in the 2005-2017 period. We then collect the time-series information on each company’s revenues for the 1990-1999 period and impute the total value of emissions for each firm by taking the product of the emission intensity coefficient and the firm’s time-varying sales. We thus obtain a panel of imputed total corporate emissions for 1990-1999. We do exactly the same for emissions over our sample period. That is, we take the emission intensity coefficient for 2017 and impute back total emissions over the 2017-2005 sample period by multiplying this coefficient with the firm’s sales year by year. This latter imputation has the additional benefit of adding imputed emissions to our sample for all the new firms added to our sample in 2016 and provides another robustness check of our findings.

Next, we estimate the regression model in (1) using the imputed emission values for both time periods and report the results in Table 16. The process of imputation is not suitable to obtain the variation in emission growth rates since changes in emissions would vary one to one with changes in revenues. We have therefore considered an alternative model in which we have fixed the growth rates at the first available reported value and used it for all dates in the 1990-1999 period. The results from this estimation, available upon request, indicate that again the carbon premium is insignificant. The results in Panel A for the period of our sample indicate that this imputation works and that there is a significant carbon premium associated with the imputed level of emissions for all three scope categories. Notably, the magnitude of the results is even stronger than for the reported emission data. In contrast, the results in Panel B for the 1990s indicate that there was no significant carbon premium over this period. This finding is consistent with the quite plausible view that investors did not yet internalize carbon risk over this time period, but began to do so in the last two decades, as reporting on climate change, the effects of global warming, technological progress in renewable energy, and political action to curb carbon emissions intensified.

# 3.7. Robustness

We have explored a number of alternatives that provide insight on the effects we document. We report the specific tables in the Online Appendix. Below, we briefly summarize the main findings in these tables.

First, we estimate the carbon premium excluding the period of the financial crisis, which we define as the period from August 2007 to July 2009. The reason for excluding the financial crisis is that during this period the level of emissions is artificially low because of the crisis and stock returns are highly volatile. As a result, the relation between stock returns and carbon emissions may be distorted by the observations from the crisis period. Broadly, we find in Table A.8 that excluding the crisis period does not affect our results in a major way.

Second, we explore the robustness of our results to the alternative GIC 6-digit industry classification. How much does this alternative classification affect changes in the estimates when industry fixed effects are included? Again, the results, reported in Table A.9, are broadly similar to those obtained under the finer Trucost industry classification. Third, we exclude the salient industries from our analysis of the carbon premium pre and post Paris Agreement. The results are reported in Table A.10. If anything, the increase in the size of the premium is more pronounced in the non-salient industries (with the exception, possibly, of scope 3 emissions).

Fourth, we split the sample into two categories of firms, those that report their emissions and those for which emissions are estimated, and contrast how the carbon premium varies across the two categories. The results are reported in Table A.11. The coefficient for the level of scope 1 emissions is slightly smaller and slightly less significant for firms that disclose their emissions than for firms that do not. This is not entirely surprising given that, other things equal, firms are more likely to disclose their emissions if their performance on that dimension is better. Alternatively, firms that go out of their way to disclose may also have taken steps to reduce their emissions.16 Overall, the carbon premium is larger and more significant for the firms that do not.

16 The magnitudes of the coefficients of the estimated emissions could also be affected by measurement error. In general, such measurement error leads to attenuation bias; irrespective of the direction of the bias our comparisons should be treated with caution in the absence of a systematic adjustment for such an error.

disclose their emissions for all categories of emissions and for both emission levels and the growth in emissions (with one exception for scope 3 emission levels).

Fifth, we estimate the premium associated with the level and intensity of all three categories of emissions added up together. This is to facilitate comparison with the results in Garvey, Iyer, and Nash (2018) and In, Park, and Monk (2019). As one might expect based on our results for the disaggregated emissions, there is a highly significant premium associated with the level of emissions, but not with emission intensity. The results are presented in Table A.12. Sixth, we also report how institutional investor portfolios are not underweight companies with high levels of emissions (or high growth rates) in Table A.4. If anything, institutional investors load up on scope 2 and scope 3 emission levels. This could be a mechanical effect of their exclusionary screening policies based on scope 1 emission intensity.

Seventh, we further report how institutional investor portfolios are affected by the level of emissions in the companies they hold outside the salient industries tied to fossil fuels. We report the results in Table A.5. Interestingly, institutional investor portfolios load up on all three scope emission levels in the non-salient industries. Again, this is likely the consequence of institutional investors’ exclusionary screening in the salient industries. If they hold less in these industries, they must hold more in other industries. Table A.13 also reports the exposure to emission levels of institutional investors’ portfolios in the salient industries. Here we observe that their portfolios do not exhibit a significant tilt away from or into firms with high emission levels (with the exception of scope 3 emissions, where they are significantly underweight).

Eighth, we explore how sensitive the carbon premium is to the addition of other firm characteristics besides size. Table A.2 reports the results. It turns out that, controlling for other firm characteristics such as B/M, PPE, leverage, etc. matters. Without these controls, there is no significant premium associated with the level of emissions; however, the growth in emissions remains highly significant). Note also that when we add industry fixed effects, adding size as a control or not affects results, with a significant premium associated with the level of scope 1 emissions appearing only when we control for size.

Ninth, we check the robustness of our ownership regressions with respect to outliers using the natural logarithm transformation. The results, in Table A.14, indicate that there is no significant difference compared to our baseline results in Table 8. Tenth, we estimate the carbon premium on only the subset of firms for which we have carbon emission data before 2016. The results are reported in Table A.15. Although the size of the premium is a little smaller, it is broadly in line with the one estimated on the full sample.

# 4. Conclusion

How is climate change affecting stock returns? This is a fundamental question for the burgeoning field of climate change and finance. It is also a fundamental question for policy makers who are seeking to enlist investors in the fight against climate change. We address this question by undertaking a cross-sectional stock returns analysis, with carbon emissions as a firm characteristic, and find robust evidence that carbon emissions significantly and positively affect stock returns. There is a straightforward link between climate change mitigation and the reduction in carbon emissions. Whether through the production of their goods and services, or through the use of their products, firms are differentially affected by policies to curb carbon emissions and by renewable-energy technology shocks. Our evidence suggests that investors are discerning these cross-sectional differences and are pricing in carbon risk. We also find that the carbon premium cannot be explained through a sin stock divestment effect. Divestment takes place in a coarse way in a few industries such as oil and gas, utilities, and automobiles, and is entirely based on scope 1 emission intensity screens. Notably, we find no carbon premium associated with emission intensity. Moreover, outside the salient industries where all the divestment takes place, we find a robust, persistent, and significant carbon premium at the firm level for all three categories of emission levels and growth rates.

18

# References

<bib id="bib1" type="Periodical">Andersson, M., Bolton P., Samama, F., 2016. Hedging climate risk. Financial Analysts Journal 72(3), 13-32.</bib>

<bib id="bib2" type="Book">Bakkensen, L., Barrage, L., 2018. Flood risk belief heterogeneity and coastal home price dynamics: Going under water? NBER Working Paper No. 23854.</bib>

<bib id="bib3" type="Periodical">Baldauf, M., Garlappi, L., Yannelis, C., 2020. Does climate change affect real estate prices? Only if you believe in it. Review of Financial Studies 33, 1256-1295.</bib>

<bib id="bib4" type="Periodical">Bernstein, A., Gustafson, M., Lewis, R., 2019. Disaster on the horizon: The price effect of sea level rise. Journal of Financial Economics 134(2), 253-272.</bib>

<bib id="bib5" type="Book">Busch T., Johnson, M., Pioch, T., 2018. Consistency of corporate carbon emission data. University of Hamburg Report WWF Deutschland, Hamburg.</bib>

<bib id="bib6" type="Periodical">Chava, S., 2014. Environmental externalities and cost of capital. Management Science 60(9), 2223-2247.</bib>

<bib id="bib7" type="Periodical">Davis, J., Fama, E. F., French, K., 2000. Characteristics, covariances, and average returns: 1929-1997. Journal of Finance 55, 389-406.</bib>

<bib id="bib8" type="Periodical">Eccles, R., Klimenko, S., 2019. The investor revolution. Harvard Business Review May-June Issue, 106-116.</bib>

<bib id="bib9" type="Periodical">Engle, R., Giglio, S., Lee, H., Kelly, B., Stroebel, J., 2020. Hedging climate change news. Review of Financial Studies 33, 1184-1216.</bib>

<bib id="bib10" type="Periodical">Fama, E. F., MacBeth, J., 1973. Risk, return, and equilibrium: Empirical tests. Journal of Political Economy 81, 607-636.</bib>

<bib id="bib11" type="Periodical">Fama, E. F., French, K., 2000. Forecasting profitability and earnings. Journal of Business 73(2), 161-175.</bib>

<bib id="bib12" type="Periodical">Giglio, S., Maggiori, M., Rao, K., Stroebel, J., Weber, A., 2018. Climate change and long-run discount rates: Evidence from real estate. Chicago Booth Research Paper No. 17-22.</bib>

<bib id="bib13" type="Periodical">Gabaix, X., 2014. A sparsity-based model of bounded rationality. Quarterly Journal of Economics 129(4), 1661–1710.</bib>

<bib id="bib14" type="Periodical">Gennaioli, N., Shleifer, A., 2010. What comes to mind. Quarterly Journal of Economics 125(4), 1399–1433.</bib>

<bib id="bib15" type="Periodical">Garvey G. T., Iyer, M., Nash, J., 2018. Carbon footprint and productivity: Does the “E” in ESG capture efficiency as well as environment? Journal of Investment Management 16(1), 59-69.</bib>

# References

<bib id="bib16" type="Book">Görgen M., Jacob, A., Nerlinger, M., Riordan, R., Rohleder, M., Wilkens, M., 2019. Carbon risk. Unpublished working paper. University of Augsburg.</bib>

<bib id="bib17" type="Periodical">Hong, H., Kacperczyk, M., 2009. The price of sin: The effects of social norms on markets. Journal of Financial Economics 93(1), 15-36.</bib>

<bib id="bib18" type="Book">Hong, H., Kubik, J., Scheinkman, J., 2012. Financial constraints on corporate goodness. NBER Working Paper No. 18476.</bib>

<bib id="bib19" type="Periodical">Hong, H., Li, F. W., Xu, J., 2019. Climate risks and market efficiency. Journal of Econometrics 208(1), 265-281.</bib>

<bib id="bib20" type="Book">Hsu, P.-H., Li, K., Tsou, CY., 2019. The pollution premium. Unpublished working paper. HKUST.</bib>

<bib id="bib21" type="Periodical">Ilhan, E., Sautner, Z., Vilkov, G., 2020. Carbon tail risk. Review of Financial Studies, forthcoming.</bib>

<bib id="bib22" type="Book">In, S. Y., Park, K. Y., Monk, A., 2019. Is 'being green' rewarded in the market? An empirical investigation of decarbonization and stock returns. Unpublished working paper. Stanford Global Project Center. https://ssrn.com/abstract=3020304</bib>

<bib id="bib23" type="Periodical">Kacperczyk, M., Van Nieuwerburgh, S., and Veldkamp, L., 2016. A rational theory of mutual funds' attention allocation. Econometrica 84(2), 571-626.</bib>

<bib id="bib24" type="Periodical">Khan M., Serafeim, G., Yoon, A., 2016. Corporate sustainability: First evidence on materiality. The Accounting Review 91(6), 1697-1724.</bib>

<bib id="bib25" type="Periodical">Krueger, P., Sautner, Z., Starks, L., 2020. The importance of climate risks for institutional investors. Review of Financial Studies 33, 1067-1111.</bib>

<bib id="bib26" type="Periodical">Matsumura, E. M., Prakash, R., and Vera-Muñoz, S. C., 2014. Firm-value effects of carbon emissions and carbon disclosures. The Accounting Review 89(2), 695-724.</bib>

<bib id="bib27" type="Periodical">Merton, R. C., 1987. A simple model of capital market equilibrium with incomplete information. Journal of Finance 42, 483–510.</bib>

<bib id="bib28" type="Book">Monasterolo, I., De Angelis, L., 2019. Blind to carbon risk? An analysis of stock market’s reaction to the Paris Agreement. Unpublished working paper. University of Bologna.</bib>

<bib id="bib29" type="Periodical">Murfin, J., Spiegel, M., 2020. Is the risk of sea level rise capitalized in residential real estate? Review of Financial Studies 33, 1217-1255.</bib>

# Panel A: Average firm emissions (scope 1 – scope 3)

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|450|400|350|300|250|200|150|100|50|0| | | | |
|Scope 2|4.5|4|3.5|3|2.5|2|1.5|1|0.5|0| | | | |
|Scope 3|21| | | | | | | | | | | | | |

# Carbon emissions: time series summary

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|0|500|1000|1500|2000|2500|3000|3500| | | | | | |
|Scope 2|0|500|1000|1500|2000|2500|3000|3500| | | | | | |
|Scope 3|0|500|1000|1500|2000|2500|3000|3500| | | | | | |

# Panel D: Total emissions (alternatives)

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Carbon direct|0|500|1000|1500|2000|2500|3000|3500| | | | | | |
|Carbon indirect|0|500|1000|1500|2000|2500|3000|3500| | | | | | |
|GHG direct|0|500|1000|1500|2000|2500|3000|3500| | | | | | |
|GHG indirect|0|500|1000|1500|2000|2500|3000|3500| | | | | | |

The data source is Trucost and the data sample period is 2005-2017. Panels A and B present average firm emissions (in tons of CO2 equivalent to revenues in $ million). The emissions are broken down into scope 1, scope 2, and scope 3 emissions. In Panel B, GHG Direct and GHG Indirect are impact ratios expressed as a percentage of costs in revenues (in $ million). Carbon direct and Carbon indirect are intensities expressed in tons of CO2 equivalent to revenues in $ million. Panels C and D present the total emissions (across all firms) per year.

22

# Fig. 2. Carbon emissions: sample selection.

The data source is Trucost. The figure presents the number of firms with valid emission data over the 2005-2017 period.

# Panel A: Unconditional data

3500300025002000150010005000

# Panel B: Within industry-variation

0.60.50.40.30.20.10

200601200609200705200809200801200905201009201001201105201201201305201209201401201505201409201601201609201705

wscope1chg wscope2chg wscope3chg

23

# Fig. 3. Standard deviation of carbon emission growth rates.

The data source is Trucost. Panel A presents the cross-sectional standard deviation of firm-level emissions. Panel B presents the cross-sectional standard deviation of firm level emissions within GIC-6 industries, all averaged across all the industries in a given year. All emissions are broken down into scope 1, scope 2, and scope 3, over the 2005-2017 period. The emission levels are measured in millions of tons of CO2 equivalent and are winsorized at the 1% level.

# Panel A: Without industry fixed effects

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|35|30|25|20|15|10|5|0|-5| | | | | |
| |Scope 2| | | | | | | | | | | | | |
| |Scope 3| | | | | | | | | | | | | |

# Panel B: With industry fixed effects

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|24| | | | | | | | | | | | | |
|Scope 2| | | | | | | | | | | | | | |
|Scope 3| | | | | | | | | | | | | | |

# Fig. 4. Carbon cumulative return premia: level effect.

Figures show the cumulative values of carbon premia estimated from the cross-sectional regressions of monthly returns on the natural logarithm of the level of scope 1, scope 2, and scope 3 emissions. The regressions include the same set of controls as in Table 7. Panel A shows the plots for the model without industry fixed effects, while Panel B shows the results with industry-fixed effects as additional control. The data source is Trucost and the sample period is 2005-2017.

# Panel A: Without industry fixed effects

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|0|10|20|30|40|50|60| | | | | | | |
|Scope 2|0|10|20|30|40|50|60| | | | | | | |
|Scope 3|0|10|20|30|40|50|60| | | | | | | |

# Panel B: With industry fixed effects

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|0|10|20|30|40|50|60| | | | | | | |
|Scope 2|0|10|20|30|40|50|60| | | | | | | |
|Scope 3|0|10|20|30|40|50|60| | | | | | | |

# Fig. 5. Carbon cumulative return premia: change effect.

Figures show the cumulative values of carbon premia estimated from the cross-sectional regressions of monthly returns on the percentage changes (year over year) of scope 1, scope 2, and scope 3 emission levels. The regressions include the same set of controls as in Table 7. Panel A shows the plots for the model without industry fixed effects, while Panel B shows the results with industry-fixed effects as additional control. The data source is Trucost and the sample period is 2005-2017.

# Panel A: Without industry fixed effects

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Scope 1|-2|0|2|4|6|8|10|12| | | | | | | |
|Scope 2|-4|-2|0|2|4|6|8|10| | | | | | | |
| |Scope 3|-6|-8|-10|-12|-14|-16|-18|-20| | | | | | |

# Panel B: With industry fixed effects

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |Scope 1| | | | | | | | | | | | | |26| |
| | |Scope 2| | | | | | | | | | | | | | |
| | |Scope 3| | | | | | | | | | | | | | |

# 10

# 8

# 6

# 4

# 2

# 0

# -2

# -4

# -6

# 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017

# Scope 1             Scope 2             Scope 3

# Fig. 6. Carbon cumulative return premia: intensity effect.

Figures show the cumulative values of carbon premia estimated from the cross-sectional regressions of monthly returns on the carbon intensity of scope 1, scope 2, and scope 3 emissions. The regressions include the same set of controls as in Table 7. Panel A shows the plots for the model without industry fixed effects, while Panel B shows the results with industry-fixed effects as additional control. The data source is Trucost and the sample period is 2005-2017.

# Panel A: Full sample

# 0

# -0.05

# -0.1

# -0.15

# -0.2

# -0.25

# -0.3

# -0.35

# -0.4

# 200501200507200601200607200701200707200801200807200901200907201001201007201101201107201201201207201301201307201401201407201501201507201601201607201701201707

# scope 1

# 27

# 5

# 4

# 3

# 2

# 1

# 0

# -1

# -2

# -3

# -4

|scope 2|scope 2|
|---|
|1.5|1|
|0.5|0|
|-0.5|-1|
|-2|-3|
|-4| |

|scope 3|scope 3|
|---|
|0.2|0.1|
|0|-0.1|
|-0.2|-0.3|
|-0.4|-0.5|

|scope 1|scope 1|
|---|
|28| |

# Scope 2

|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1.6|1.4|1.2|1.0|0.8|0.6|0.4|0.2|0.0|-0.2|-0.4|-0.6| | |

# Scope 3

|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0.2|0.1|0.0|-0.1|-0.2|-0.3|-0.4|-0.5| | | | | | |

# Scope 1

|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|
|---|---|---|---|---|---|---|---|---|---|---|---|
| |29| | | | | | | | | | |

# Fig. 7. Carbon intensity and institutional ownership: cumulative effect.

Figures show the cumulative values of the coefficient of emission intensity estimated from the cross-sectional regressions of monthly firm-level institutional ownership on scope 1, scope 2, and scope 3 emissions intensity. The regressions include the same set of controls as Table 11. Panel A shows the plots for the full sample, Panel B shows the results for the sample of firms excluding salient industries (GIC 19, 20, 23), Panel C shows the results for the sample of firms excluding the same salient industries and also firms that are added to the sample post 2015. The data source is Trucost and the sample period is 2005-2017.

# Table 1. Summary statistics.

This table reports summary statistics (averages, medians, and standard deviations) for the variables used for the six sets of regressions. The sample period is 2005-2017. Panel A reports the emission variables. Panel B reports the cross-sectional return variables. RET is the monthly stock return; LOGSIZE is the natural logarithm of market capitalization (in $ million); B/M is the book value of equity divided by market value of equity; ROE is the return on equity; LEVERAGE is the book value of leverage defined as the book value of debt divided by the book value of assets; MOM is the cumulative stock return over the one-year period; INVEST/A is the CAPEX divided by book value of assets; HHI is the Herfindahl index of the business segments of a company with weights proportional to revenues; LOGPPE is the natural logarithm of plant, property & equipment (in $ million); BETA is the

CAPM beta calculated over the one year period; VOLAT is the monthly stock return volatility calculated over the one year period. Panel C reports the time-series variables. MKTRF is the monthly return on the value-weighted stock market net of the risk free rate; HML is the monthly return on the portfolio long value stocks and short growth stocks; SMB is the monthly return on the portfolio long small-cap stocks and short large-cap stocks; MOM is the monthly return on the portfolio long 12-month stock winners and short 12-month past losers; CMA is the monthly return of a portfolio that is long on conservative investment stocks and short on aggressive investment stocks; BAB is the monthly return of a portfolio that is long on low-beta stocks and short on high-beta stocks; LIQ is the liquidity factor of Pastor and Stambaugh; NET ISSUANCE is the monthly return of a portfolio that is long on high-net-issuance stocks and short on low-net-issuance stocks. Net issuance for year t is the change in the natural log of split-adjusted shares outstanding from the fiscal yearend in t-2 to the fiscal yearend in t-1; IDIO VOL is the monthly return of a portfolio that is long on low idiosyncratic volatility stocks and short on high idiosyncratic volatility stocks. Panel D reports the ownership variables. IOi,t is the fraction of the shares of company i held by institutions in the FactSet database at the end of year t. IO is calculated by aggregating the shares held by all types of institutions at the end of the year, and then dividing this amount by shares outstanding at the end of the year. IO_BANKS is the ownership by banks; IO_INSURANCE is the ownership by insurance companies; IO_INVESTCOS is the ownership by investment companies (e.g., mutual funds); IO_ADVISERS is the ownership by independent investment advisers; IO_PENSIONS is the ownership by pension funds; IO_HFS is the ownership by hedge funds. PRINVi,t is the inverse of firm i’s share price at the end of year t; TOT VOLATi,t is the standard deviation of daily stock returns for company i over the one-year period; VOLUMEi,t is the average daily trading volume (in $million) of stock i over the calendar year t; NASDAQi,t is an indicator variable equal to one if a stock i is listed on NASDAQ in year t, and zero otherwise; SP500i,t is an indicator variable equal to one if a stock i is part of the S&P 500 Index in year t, and zero otherwise.

# Panel A: Emission variables

|Variable|Mean|Median|Std. Dev.|
|---|---|---|---|
|Log (Carbon Emissions Scope 1 (tons COe))2|10.55|10.47|2.95|
|Log (Carbon Emissions Scope 2 (tons COe))2|10.52|10.66|2.36|
|Log (Carbon Emissions Scope 3 (tons COe))2|12.31|12.46|2.25|
|Growth Rate in Carbon Emissions Scope 1 (winsorized at 2.5%)|0.08|0.03|0.36|
|Growth Rate in Carbon Emissions Scope 2 (winsorized at 2.5%)|0.14|0.05|0.45|
|Growth Rate in Carbon Emissions Scope 3 (winsorized at 2.5%)|0.09|0.06|0.24|
|Carbon Intensity Scope 1 (tons COe/USD m.)/100 (winsorized at 2.5%)2|1.92|0.15|5.88|
|Carbon Intensity Scope 2 (tons COe/USD m.)/100 (winsorized at 2.5%)2|0.34|0.18|0.46|
|Carbon Intensity Scope 3 (tons COe/USD m.) /100 (winsorized at 2.5%)2|1.58|0.98|1.59|
|Carbon Intensity Direct (winsorized at 2.5%)/100|2.12|0.16|6.45|
|Carbon Intensity Indirect (winsorized at 2.5%)/100|1.04|0.58|1.31|
|GHG Direct Impact Ratio (winsorized at 2.5%)|0.75|0.06|2.29|
|GHG Indirect Impact Ratio (winsorized at 2.5%)|0.71|0.47|0.68|

# Panel B: Cross-sectional return variables

|Variable|Mean|Median|Std. Dev.|
|---|---|---|---|
|RET (%)|1.14|1.08|10.84|
|LOGSIZE|8.25|8.25|1.57|

|B/M (winsorized at 2.5%)|0.50|0.39|0.41|
|---|---|---|---|
|LEVERAGE (winsorized at 2.5%)|0.24|0.22|0.18|
|MOM (winsorized at 0.5%)|0.15|0.11|0.45|
|INVEST/A (winsorized at 2.5%)|0.05|0.03|0.05|
|ROE (winsorized at 2.5%, in %)|9.76|11.32|21.23|
|HHI|0.82|1.00|0.24|
|LOGPPE|6.22|6.34|2.26|
|BETA|1.10|1.05|0.44|
|VOLAT (winsorized at 0.5%)|0.10|0.08|0.06|
|SALESGR (winsorized at 0.5%)|0.02|0.03|0.30|
|EPSGR (winsorized at 0.5%)|0.01|0.00|0.43|

# Panel C: Time-series variables

|MKTRF (in %)|0.70|1.06|4.08|
|---|---|---|---|
|HML (in %)|0.00|-0.22|2.57|
|SMB (in %)|0.07|0.04|2.26|
|MOM (in %)|0.07|0.36|4.53|
|CMA (in %)|0.02|-0.06|1.39|
|BAB (in %)|0.49|0.74|2.66|
|LIQ (in %)|0.15|0.38|3.59|
|NET ISSUANCE (in %)|0.51|0.55|1.65|
|IDIO VOL (in %)|-0.18|0.03|5.27|

# Panel D: Ownership variables

|IO (in %)|76.84|82.93|22.22|
|---|---|---|---|
|IO_BANKS (in %)|0.10|0.07|0.16|
|IO_INSURANCE (in %)|0.35|0.13|3.11|
|IO_INVESTCOS. (in %)|18.19|18.37|8.64|
|IO_ADVISERS (in %)|43.94|46.11|15.39|
|IO_PENSIONS (in %)|3.40|3.51|2.31|
|IO_HFS (in %)|10.87|7.73|10.04|
|PRINV (winsorized at 0.5%)|0.05|0.03|0.11|

# Table 2. Stock characteristics by emission calculation.

The table reports the sample means of the main variables over the 2005-2017 period. All variables are defined in Table 1. Imputed includes all firms for which Trucost estimates the levels of emissions. Direct includes all firms for which data is directly available.

|Calculation Method|Imputed|Direct|
|---|---|---|
|SCOPE 1 TOT|1366013|5954876|
|SCOPE 2 TOT|264203|957827|
|SCOPE 3 TOT|1433741|4057516|
|SCOPE 1 INT|211.76|588.91|
|SCOPE 2 INT|35.89|68.26|
|SCOPE 3 INT|158.11|197.92|
|RET (%)|1.00|1.09|
|LOGSIZE|8.22|9.64|
|B/M|0.50|0.48|
|LEVERAGE|0.24|0.27|
|MOM|0.15|0.13|
|INVEST/A|0.05|0.05|
|ROE|9.88|14.89|
|HHI|0.84|0.72|
|LOGPPE|6.19|8.03|
|BETA|1.13|1.04|
|VOLAT|0.10|0.07|
|SALESGR (%)|1.67|-0.16|

# Table 3. Carbon emissions: correlations.

The sample period is 2005-2017. Panel A presents the cross-correlations among emission variables. Panel B presents the coefficients from estimating the AR(1) model for various measures of emissions. All regressions include year-month fixed effects. We cluster standard errors at firm and year dimensions. The emission variables are defined in Table 1. ***1% significance; **5% significance; *10% significance.

# Panel A: Cross-correlations

| |SCOPE 1 TOT|SCOPE 2 TOT|SCOPE 3 TOT|SCOPE 1 INT|SCOPE 2 INT|SCOPE 3 INT|
|---|---|---|---|---|---|---|
|SCOPE 1 TOT|1.00| | | | | |
|SCOPE 2 TOT|0.39|1.00| | | | |
|SCOPE 3 TOT|0.51|0.75|1.00| | | |
|SCOPE 1 INT|0.60|0.03|0.03|1.00| | |
|SCOPE 2 INT|0.05|0.24|0.02|0.10|1.00| |
|SCOPE 3 INT|0.21|0.09|0.27|0.25|0.10|1.00|

# Panel B: Autocorrelations

|VARIABLES|(1) LOG (SCOPE 1)|(2) LOG (SCOPE 2)|(3) LOG (SCOPE 3)|(4) SCOP E 1|(5) SCOP E 2|(6) SCOP E 3|(7) SCOPE 1 INT|(8) SCOPE 2 INT|(9) SCOPE 3 INT|
|---|---|---|---|---|---|---|---|---|---|
|LOG (SCOPE 1 TOT)t-1|0.977***| | | | | | | | |
|LOG (SCOPE 2 TOT)t-1| |0.955***| | | | | | | |
|LOG (SCOPE 3 TOT)t-1| | |0.967***| | | | | | |
|SCOPE 1t-1| | | |0.045*| | | | | |
|SCOPE 2t-1| | | | |0.025| | | | |

# Table 4

# Carbon emissions over time.

The table reports the cross-sectional averages of scope 1, scope 2, and scope 3 levels and intensity variables over the 2005-2017 period. Panel A considers a full sample of firms. Panel B is restricted to a sample of firms that existed prior to 2016. The emissions variables are defined in Table 1.

# Panel A: Full sample

|Year|SCOPE 1 TOT|SCOPE 2 TOT|SCOPE 3 TOT|SCOPE 1 INT|SCOPE 2 INT|SCOPE 3 INT|
|---|---|---|---|---|---|---|
|2005|2697225|335402|2414925|411.16|37.55|229.79|
|2006|2775999|379869|2229797|373.64|39.17|205.90|
|2007|2893335|410656|2281158|341.57|37.38|193.13|
|2008|3147450|683294|2750231|308.70|39.75|164.33|
|2009|2482940|385670|1907531|334.35|41.41|184.06|
|2010|2655585|400848|1987772|339.68|40.47|173.56|
|2011|2639823|440716|2217712|305.06|40.20|169.39|
|2012|2417298|431992|2222692|308.23|39.57|160.65|

# Table 5

Industry representation by number of firms.

The table reports the distribution of unique firms in our sample with regard to GIC 6 industry classification. Total represents the total number of firms in our sample. The sample period is 2005-2017.

|GIC 6|Industry Name|# of Firms|
|---|---|---|
|1|Energy Equipment & Services|75|
|2|Oil, Gas & Consumable Fuels|164|
| | |36|

# Panel B: Legacy sample

|Year|SCOPE 1 TOT|SCOPE 2 TOT|SCOPE 3 TOT|SCOPE 1 INT|SCOPE 2 INT|SCOPE 3 INT|
|---|---|---|---|---|---|---|
|2005|2697225|335402|2414925|411.16|37.55|229.79|
|2006|2775999|379869|2229797|373.64|39.17|205.90|
|2007|2893335|410656|2281158|341.57|37.38|193.13|
|2008|3147450|683294|2750231|308.70|39.75|164.33|
|2009|2482940|385670|1907531|334.35|41.41|184.06|
|2010|2655585|400848|1987772|339.68|40.47|173.56|
|2011|2639823|440716|2217712|305.06|40.20|169.39|
|2012|2417298|431992|2222692|308.23|39.57|160.65|
|2013|2223849|398491|2046741|335.82|39.22|159.69|
|2014|2255386|425080|1979578|281.89|54.37|152.26|
|2015|2161598|419362|1783537|273.32|56.79|150.77|
|2016|1993060|404850|1874254|269.09|45.78|167.35|
|2017|1922550|404904|2149459|243.38|44.95|176.12|

# 3 Chemicals

81

# 4 Construction Materials

17

# 5 Containers & Packaging

21

# 6 Metals & Mining

47

# 7 Paper & Forest Products

12

# 8 Aerospace & Defence

46

# 9 Building Products

32

# 10 Construction & Engineering

36

# 11 Electrical Equipment

54

# 12 Industrial Conglomerates

16

# 13 Machinery

118

# 14 Trading Companies & Distributors

40

# 15 Commercial Services & Supplies

69

# 16 Professional Services

42

# 17 Air Freight & Logistics

15

# 18 Airlines

13

# 19 Marine

27

# 20 Road & Rail

31

# 21 Transportation Infrastructure

5

# 22 Auto Components

43

# 23 Automobiles

8

# 24 Household Durables

64

# 25 Leisure Products

21

# 26 Textiles, Apparel & Luxury Goods

41

# 27 Hotels, Restaurants & Leisure

95

# 28 Diversified Consumer Services

38

# 29 Media

83

# 30 Distributors

8

# 31 Internet & Direct Marketing Retail

45

# 32 Multiline Retail

17

# 33 Specialty Retail

110

37

# 34  Food & Staples Retailing

27

# 35  Beverages

17

# 36  Food Products

57

# 37  Tobacco

9

# 38  Household Products

12

# 39  Personal Products

15

# 40  Health Care Equipment & Supplies

109

# 41  Health Care Providers & Services

77

# 42  Health Care Technology

20

# 43  Biotechnology

203

# 44  Pharmaceuticals

87

# 45  Life Sciences Tools & Services

34

# 46  Banks

260

# 47  Thrifts & Mortgage Finance

61

# 48  Diversified Financial Services

28

# 49  Consumer Finance

37

# 50  Capital Markets

92

# 51  Mortgage Real Estate Investment Trusts (REITs)

22

# 52  Insurance

111

# 53  Internet Software & Services

100

# 54  IT Services

102

# 55  Software

150

# 56  Communications Equipment

47

# 57  Technology Hardware, Storage & Peripherals

34

# 58  Electronic Equipment, Instruments & Components

82

# 59  Semiconductors & Semiconductor Equipment

103

# 60  Diversified Telecommunication Services

34

# 61  Wireless Telecommunication Services

15

# 62  Media

49

# 63  Entertainment

22

# 64  Interactive Media & Services

29

# Table 6

# Carbon emission production by industry.

Panel A reports the top 10 of GIC 6 industries in terms of average emission production (scope 1, scope 2, scope 3). Panel B reports the bottom 10 of GIC 6 industries in terms of average emission production (scope 1, scope 2, scope 3). The sample period is 2005-2017. The emission variables are expressed in tons of CO2e.

# Panel A: Largest emissions (avg.)

|GIC 6|Scope 1|GIC 6|Scope 2|GIC 6|Scope 3|
|---|---|---|---|---|---|
|69|33300000|34|2163081|23|18700000|
|65|30700000|23|2094174|36|11800000|
|18|17600000|6|1749360|37|6847386|
|67|17200000|3|1475783|12|6575213|
|6|6343545|7|1375637|35|6106099|
|2|6302663|60|1219956|2|6049237|
|17|4316221|12|1014037|34|5882429|
|4|3827648|38|994783|38|4313762|
|7|3286922|32|825501|6|3580245|
|3|3280770|2|820777|22|3285134|

# Panel B: Smallest emissions (avg.)

|GIC 6|Scope 1|GIC 6|Scope 2|GIC 6|Scope 3|
|---|---|---|---|---|---|
|47|601|47|1756|47|15193|
|50|6767|42|11824|51|27069|
|46|6965|19|21798|68|41182|
|49|7469|16|22653|42|64097|

# Table 7

# Determinants of carbon emissions.

The sample period is 2005-2017. The dependent variables are natural logarithm of total emissions, percentage change in total emissions, and carbon intensity. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the firm level and year (in parentheses). All regressions include year-month fixed effects and industry-fixed effects. ***1% significance; **5% significance; *10% significance.

|Variables|LOG (SCOPE 1)|LOG (SCOPE 2)|LOG (SCOPE 3)|ΔSCOPE 1|ΔSCOPE 2|ΔSCOPE 3|SCOPE 1 INT|SCOPE 2 INT|SCOPE 3 INT|
|---|---|---|---|---|---|---|---|---|---|
|LOGSIZE|0.438***|0.571***|0.572***|0.026***|0.026***|0.027***|-0.118*|0.002|-0.021**|
| |(0.036)|(0.032)|(0.022)|(0.008)|(0.008)|(0.006)|(0.063)|(0.006)|(0.009)|
|B/M|0.464***|0.555***|0.562***|-0.033**|-0.038|-0.041**|-0.003|0.003|0.000|
| |(0.060)|(0.059)|(0.054)|(0.015)|(0.021)|(0.017)|(0.107)|(0.010)|(0.013)|
|ROE|0.006***|0.006***|0.007***|-0.002***|-0.002***|-0.001***|-0.002|-0.000|0.000|
| |(0.001)|(0.001)|(0.001)|(0.000)|(0.001)|(0.000)|(0.002)|(0.000)|(0.000)|
|LEVERAGE|0.531**|0.625***|0.574***|0.026|0.010|0.019|0.364|0.002|-0.056*|
| |(0.196)|(0.188)|(0.162)|(0.020)|(0.030)|(0.023)|(0.230)|(0.030)|(0.030)|
|INVEST/A|-2.026***|-1.950***|-2.457***|0.676***|0.706***|0.530***|-0.586|-0.067|-0.446**|
| |(0.489)|(0.460)|(0.432)|(0.145)|(0.132)|(0.117)|(1.161)|(0.153)|(0.201)|
|HHI|-1.044***|-0.569***|-0.499***|0.014|-0.024|0.023**|-2.185***|0.009|-0.260***|
| |(0.119)|(0.081)|(0.063)|(0.021)|(0.024)|(0.008)|(0.497)|(0.030)|(0.062)|
|LOGPPE|0.376***|0.372***|0.317***|-0.033***|-0.034***|-0.030***|0.127***|0.025***|0.026***|
| |(0.036)|(0.037)|(0.023)|(0.005)|(0.006)|(0.006)|(0.042)|(0.007)|(0.007)|
|SALESGR|0.237***|0.190**|0.231**|0.311***|0.343***|0.320***|-0.085|-0.019**|0.010|
| |(0.059)|(0.062)|(0.077)|(0.042)|(0.041)|(0.030)|(0.070)|(0.007)|(0.024)|

# Table 8

# Carbon emissions and stock returns.

The sample period is 2005-2017. The dependent variable is RET. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the firm and year level (in parentheses). All regressions include year-month fixed effects. In the regressions for columns 4 through 6, we additionally include industry-fixed effects. Panel A reports the results for the natural logarithm of total firm-level emissions; Panel B reports the results for the percentage change in carbon total emissions; Panel C reports the results for carbon emission intensity. ***1% significance; **5% significance; *10% significance.

# Panel A: Total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|LOG (SCOPE 1 TOT)|0.043**| | |0.164***| | |
| |(0.023)| | |(0.036)| | |
|LOG (SCOPE 2 TOT)| | |0.098**| |0.167***| |
| | | |(0.042)| |(0.048)| |
|LOG (SCOPE 3 TOT)| | | |0.135**| |0.312***|
| | | | |(0.046)| |(0.071)|
|LOGSIZE|-0.140|-0.184|-0.193|-0.302*|-0.327*|-0.410**|
| |(0.163)|(0.167)|(0.165)|(0.148)|(0.154)|(0.163)|
|B/M|0.460|0.469|0.444|0.656**|0.642**|0.562**|
| |(0.260)|(0.266)|(0.258)|(0.234)|(0.229)|(0.224)|
|LEVERAGE|-0.559*|-0.579*|-0.498*|-0.699***|-0.712***|-0.790***|
| |(0.272)|(0.280)|(0.274)|(0.177)|(0.171)|(0.167)|
|MOM|0.321|0.348|0.338|0.284|0.294|0.301|
| |(0.276)|(0.272)|(0.274)|(0.291)|(0.290)|(0.290)|
|INVEST/A|-2.218|-1.914|-1.587|0.277|0.267|0.699|
| |(1.740)|(1.794)|(1.838)|(2.111)|(2.126)|(2.082)|
|ROE|0.010*|0.009|0.008|0.009*|0.009*|0.007*|
| |(0.005)|(0.005)|(0.005)|(0.004)|(0.004)|(0.004)|

# Panel A: Regression results

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|HHI|0.032|-0.026|0.137|0.130*|0.052|0.111|
| |(0.110)|(0.112)|(0.101)|(0.072)|(0.073)|(0.071)|
|LOGPPE|-0.015|-0.027|-0.045|0.020|0.019|-0.017|
| |(0.100)|(0.088)|(0.090)|(0.058)|(0.058)|(0.057)|
|BETA|0.059|0.023|0.047|0.045|0.040|0.063|
| |(0.131)|(0.131)|(0.130)|(0.148)|(0.147)|(0.146)|
|VOLAT|0.978|0.674|0.749|0.622|0.501|0.549|
| |(3.571)|(3.415)|(3.506)|(3.290)|(3.285)|(3.269)|
|SALESGR|0.692|0.688|0.672|0.679|0.686|0.648|
| |(0.429)|(0.430)|(0.420)|(0.412)|(0.412)|(0.407)|
|EPSGR|0.592**|0.589**|0.575**|0.637**|0.636**|0.615**|
| |(0.234)|(0.231)|(0.232)|(0.231)|(0.233)|(0.227)|

Year/month F.E. Yes Yes Yes Yes Yes Yes

Industry F.E. No No No Yes Yes Yes

Observations 184,288 184,216 184,384 184,288 184,216 184,384

R-squared 0.203 0.204 0.204 0.206 0.206 0.206

# Panel B: Growth rate in total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|ΔSCOPE 1|0.641***| | |0.627***| | |
| |(0.153)| | |(0.144)| | |
|ΔSCOPE 2| |0.345**| |0.321**| | |
| | |(0.125)| |(0.120)| | |
|ΔSCOPE 3| | |1.203***| |1.186***| |
| | | |(0.318)| |(0.314)| |
|LOGSIZE|-0.023|-0.013|-0.037|-0.107|-0.099|-0.121|
| |(0.110)|(0.112)|(0.111)|(0.114)|(0.115)|(0.117)|
|B/M|0.391|0.388|0.410*|0.771**|0.764**|0.789***|
| |(0.232)|(0.233)|(0.226)|(0.257)|(0.257)|(0.246)|
|LEVERAGE|-0.433*|-0.414*|-0.441*|-0.794***|-0.785***|-0.799***|
| |(0.217)|(0.216)|(0.213)|(0.213)|(0.217)|(0.214)|
|MOM|0.204|0.217|0.166|0.160|0.175|0.124|
| |(0.265)|(0.268)|(0.267)|(0.264)|(0.266)|(0.264)|
|INVEST/A|-2.508|-2.244|-2.638|-0.620|-0.463|-0.807|

# Panel C: Emission intensity

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|SCOPE 1 INT|-0.010| | |0.005| | |
| |(0.012)| | |(0.006)| | |
|SCOPE 2 INT| |0.145| |0.081| | |
| | |(0.121)| |(0.074)| | |
|SCOPE 3 INT| | |0.055| |0.048| |
| | | |(0.033)| |(0.075)| |
|LOGSIZE|-0.154|-0.133|-0.124|-0.229|-0.230|-0.229|
| |(0.169)|(0.159)|(0.164)|(0.142)|(0.141)|(0.142)|
|B/M|0.456|0.470|0.479*|0.732**|0.732**|0.732**|
| |(0.264)|(0.269)|(0.258)|(0.244)|(0.243)|(0.244)|
|LEVERAGE|-0.545*|-0.558*|-0.532*|-0.608***|-0.606***|-0.603***|
| |(0.264)|(0.269)|(0.263)|(0.195)|(0.195)|(0.196)|

# Table 9

Carbon emissions and stock returns net of earnings returns.

The sample period is 2005-2017. The dependent variable is RET net of daily return realized on the earnings announcement day. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the firm and year level (in parentheses). All regressions include year-month fixed effects. In the regressions for columns 4 through 6, we additionally include industry-fixed effects. Panel A reports the results for the natural logarithm of total emissions; Panel B reports the results for the percentage change in carbon total emissions; Panel C reports the results for carbon emission intensity. ***1% significance; **5% significance; *10% significance.

# Panel A: Total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|MOM|0.332|0.321|0.317|0.282|0.282|0.281|
| |(0.277)|(0.279)|(0.279)|(0.292)|(0.292)|(0.291)|
|INVEST/A|-1.953|-2.047|-1.916|-0.041|-0.037|-0.022|
| |(1.815)|(1.823)|(1.867)|(2.123)|(2.127)|(2.134)|
|ROE|0.010*|0.010*|0.010*|0.010**|0.010**|0.010**|
| |(0.005)|(0.005)|(0.005)|(0.004)|(0.004)|(0.004)|
|HHI|-0.139|-0.069|0.028|-0.032|-0.043|-0.030|
| |(0.137)|(0.113)|(0.082)|(0.074)|(0.072)|(0.067)|
|LOGPPE|0.034|0.010|0.006|0.081|0.079|0.080|
| |(0.099)|(0.087)|(0.093)|(0.065)|(0.064)|(0.066)|
|BETA|0.047|0.045|0.051|0.035|0.034|0.036|
| |(0.131)|(0.131)|(0.131)|(0.148)|(0.148)|(0.148)|
|VOLAT|1.027|0.978|1.028|0.577|0.558|0.572|
| |(3.512)|(3.527)|(3.563)|(3.296)|(3.297)|(3.300)|
|SALESGR|0.709|0.714|0.712|0.718|0.719|0.717|
| |(0.435)|(0.432)|(0.427)|(0.414)|(0.413)|(0.413)|
|EPSGR|0.600**|0.600**|0.600**|0.660**|0.660**|0.661**|
| |(0.234)|(0.232)|(0.232)|(0.235)|(0.236)|(0.235)|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|184,384|184,384|184,384|184,384|184,384|184,384|
|R-squared|0.203|0.203|0.203|0.206|0.206|0.206|

# Panel A: Total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|LOG (SCOPE 2 TOT)|0.088**|0.150***| | | | |
| |(0.040)|(0.044)| | | | |
|LOG (SCOPE 3 TOT)| |0.121**|0.279***| | | |
| | |(0.047)|(0.067)| | | |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|184,288|184,216|184,384|184,288|184,216|184,384|
|R-squared|0.220|0.221|0.220|0.223|0.223|0.223|

# Panel B: Growth rate in total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|ΔSCOPE 1|0.552***| | |0.532***| | |
| |(0.137)| | |(0.131)| | |
|ΔSCOPE 2| |0.288**| |0.266**| | |
| | |(0.111)| |(0.108)| | |
|ΔSCOPE 3| | |0.896**| |0.882**| |
| | | |(0.313)| | |(0.316)|
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|153,051|152,955|153,123|153,051|152,955|153,123|
|R-squared|0.235|0.236|0.235|0.239|0.239|0.239|

# Panel C: Emission intensity

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|SCOPE 1 INT|-0.008| | |0.004| | |
| |(0.011)| | |(0.007)| | |
|SCOPE 2 INT| |0.155| |0.079| | |
| | |(0.124)| |(0.068)| | |
|SCOPE 3 INT| | |0.050| |0.029| |
| | | |(0.032)| | |(0.071)|
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|

# Table 10

# Can the carbon premium be explained by risk factors?

The sample period is 2005-2017. The dependent variable is the monthly carbon premium estimated each period using a cross-sectional return regression. All variables are defined in Table 1. We report the results of the time-series regression with standard errors adjusted for autocorrelation with 12 lags using Newey-West test (in parentheses). Panel A reports the results for the natural logarithm of contemporaneous total emissions; Panel B reports the results for the percentage change in carbon emissions; Panel C reports the results for carbon emission intensity. ***1% significance; **5% significance; *10% significance.

# Panel A: Total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|LOG (SCOPE 1 TOT)|-1.176|3.298***|3.429**|(0.714)|(1.084)|(1.357)|
|HML|-6.020***|-4.284**|-6.444**|(1.598)|(1.759)|(2.537)|
|SMB|-0.331|1.184|1.539|(0.887)|(2.858)|(1.840)|
|MOM|0.399|-3.853**|-3.580***|(0.559)|(1.721)|(1.281)|
|CMA|0.086***|0.053|0.116***|(0.028)|(0.036)|(0.036)|
|BAB|0.772|0.303|1.581|(0.824)|(1.749)|(1.681)|
|LIQ|2.658***|0.816|3.094***|(0.768)|(1.135)|(1.016)|
|NET ISSUANCE|1.250|-1.603|0.376|(1.015)|(2.207)|(2.352)|
|IDIO VOL|1.566**|0.986|0.414| | | |

| |(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|MKTRF|4.847|-2.463|8.303| | | |
| |(5.605)|(2.516)|(8.965)| | | |
|HML|-8.427**|-5.897*|-17.483**| | | |
| |(3.853)|(3.362)|(7.113)| | | |
|SMB|-15.284**|-9.960*|-23.109*| | | |
| |(6.419)|(5.667)|(13.738)| | | |
|MOM|3.223|3.703|9.171| | | |
| |(4.704)|(2.727)|(8.912)| | | |
|CMA|-0.159*|-0.153***|-0.468***| | | |
| |(0.087)|(0.058)|(0.168)| | | |
|BAB|-8.919***|2.396|11.861| | | |
| |(3.255)|(2.036)|(8.199)| | | |
|LIQ|0.808|-1.343|9.512*| | | |
| |(2.495)|(2.342)|(4.847)| | | |
|NET ISSUANCE|4.702|1.724|15.976| | | |
| |(5.262)|(4.821)|(13.211)| | | |
|IDIO VOL|3.851|6.477*|16.111| | | |
| |(6.820)|(3.474)|(11.811)| | | |
|Constant|0.640***|0.643***|0.435***|0.463***|1.559***|1.424***|

Panel B: Growth rate in total emissions

Observations: 156

Industry adj.: No

Adj. R2: 0.001, 0.331, 0.001, 0.335, 0.001, 0.247

# Panel C: Emission intensity

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|MKTRF|-0.793***| |1.790| |0.820| |
| |(0.177)| |(2.810)| |(0.880)| |
|HML|-0.927***| |-6.181| |-4.063**| |
| |(0.315)| |(4.340)| |(1.635)| |
|SMB|-1.027**| |-9.486| |-0.722| |
| |(0.519)| |(6.371)| |(1.214)| |
|MOM|0.855***| |-1.195| |-0.449| |
| |(0.214)| |(2.970)| |(0.597)| |
|CMA|0.001| |0.008| |0.039| |
| |(0.007)| |(0.101)| |(0.031)| |
|BAB|0.302| |-4.055| |-0.645| |
| |(0.391)| |(3.961)| |(0.915)| |
|LIQ|0.229| |0.372| |2.608***| |
| |(0.297)| |(2.942)| |(0.800)| |
|NET ISSUANCE|0.445| |-6.006| |-0.139| |
| |(0.304)| |(5.742)| |(1.159)| |
|IDIO VOL|0.333| |8.908***| |0.424| |
| |(0.293)| |(3.069)| |(0.723)| |
|Constant|-0.006|-0.004|0.121|0.181*|0.018|0.012|
| |(0.008)|(0.007)|(0.102)|(0.097)|(0.027)|(0.028)|

Industry adj. No

Observations 144

# Table 11

# Carbon emissions and institutional ownership.

The sample period is 2005-2017. The dependent variable in Panel A is IO. The dependent variables in Panel B, Panel C, and Panel D are IO_BANK, IO_INSURANCE, IO_INVESTCOS, IO_ADVISERS, IO_PENSIONS, and IO_HFS. Panels A-D present the result for contemporaneous measures of emission intensity. Panel B presents the results for SCOPE 1, Panel C presents the results for SCOPE 2, and Panel D presents the results for SCOPE 3. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the industry and year level (in parentheses). All regressions include year-month fixed effects. In Panel A, the regressions for columns 2, 4, and 6 additionally include state-fixed effects. All regressions in Panels B-D include state fixed effects. ***1% significance; **5% significance; *10% significance.

# Panel A: Aggregate ownership (Emission intensity)

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|SCOPE 1 INT|-0.194**|-0.218**| | | | |
| |(0.085)|(0.083)| | | | |
|SCOPE 2 INT| | | |-0.383|-0.381| |
| | | |(1.621)|(1.610)| | |
|SCOPE 3 INT| | | | |0.094|-0.130|
| | | | | |(0.550)|(0.581)|
|LOGSIZE|2.078|1.847|2.096|1.859|2.104|1.850|
| |(1.510)|(1.702)|(1.484)|(1.678)|(1.499)|(1.706)|
|PRINV|-29.353***|-37.098***|-29.333***|-37.161***|-29.308***|-37.200***|
| |(5.614)|(6.448)|(5.611)|(6.392)|(5.640)|(6.476)|
|MOM|-1.453|-1.792*|-1.542|-1.871**|-1.544|-1.858*|
| |(0.937)|(0.876)|(0.895)|(0.823)|(0.920)|(0.856)|
|B/M|-1.165|-0.890|-1.533|-1.205|-1.498|-1.216|
| |(1.423)|(1.602)|(1.366)|(1.541)|(1.339)|(1.549)|
|BETA|9.123***|9.470***|9.332***|9.705***|9.300***|9.695***|
| |(1.508)|(1.459)|(1.421)|(1.375)|(1.430)|(1.388)|
|VOLAT|-7.617|4.118|-6.867|4.770|-7.095|4.532|

# Table 12

# Carbon emissions and stock returns: excluding salient industries.

The sample period is 2005-2017. The dependent variable is RET. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the industry level (in parentheses). The sample excludes companies in the oil and gas (gic=2), utilities (gic=65-69), and transportation (gic=18, 19, 23) industries. All regressions include year-month fixed effects. In the regressions for columns 4-6, we additionally include industry-fixed effects. Panel A reports the results for the natural logarithm of total emissions; Panel B reports the results for the percentage change in carbon emissions; Panel C reports the results for carbon emission intensity. ***1% significance; **5% significance; *10% significance.

| |(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|Variables|Banks|Insurance|Invest. Cos.|Advisers|Pensions|Hedge Funds|
|SCOPE 1 INT|0.001**|-0.011*|0.026|-0.258***|-0.009*|0.033|
| |(0.000)|(0.005)|(0.022)|(0.056)|(0.004)|(0.028)|
|SCOPE 2 INT|0.009|-0.253|-0.139|-0.156|0.049|0.108|
| |(0.006)|(0.144)|(0.406)|(0.992)|(0.097)|(0.441)|
|SCOPE 3 INT|0.004*|-0.021|0.038|0.052|0.028|-0.230|
| |(0.002)|(0.071)|(0.115)|(0.409)|(0.030)|(0.151)|
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|State fixed effect|Yes|Yes|Yes|Yes|Yes|Yes|
|Observations|160,406|160,406|160,406|160,406|160,406|160,406|

| |(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|Variables|Volume|NASDAQ|SP500|Year/month F.E.|State fixed effect|Observations|
| |-4.427***|-1.159|2.559|Yes|No|170,701|
| |(1.400)|(1.467)|(2.120)| | | |
| |-4.612**|-1.529|1.711|Yes|Yes|160,406|
| |(1.636)|(1.700)|(2.093)| | | |
| |-4.379***|-0.875|2.418|Yes|No|170,701|
| |(1.422)|(1.431)|(2.122)| | | |
| |-4.568**|-1.255|1.508|Yes|Yes|160,406|
| |(1.650)|(1.638)|(2.088)| | | |
| |-4.389***|-0.751|2.394|Yes|No|170,701|
| |(1.378)|(1.303)|(2.129)| | | |
| |-4.582**|-1.292|1.510|Yes|Yes|160,406|
| |(1.626)|(1.505)|(2.095)| | | |

# Panel A: Total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|LOG (SCOPE 1 TOT)|0.072**| | |0.177***| | |
| |(0.025)| | |(0.044)| | |
|LOG (SCOPE 2 TOT)| |0.097**| |0.227***| | |
| | |(0.039)| |(0.057)| | |
|LOG (SCOPE 3 TOT)| | |0.117**| |0.324***| |
| | | |(0.048)| |(0.074)| |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|164,094|164,166|164,190|164,094|164,166|164,190|
|R-squared|0.213|0.213|0.213|0.216|0.216|0.216|

# Panel B: Growth rate in total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|ΔSCOPE 1|0.657***| | |0.630***| | |
| |(0.151)| | |(0.142)| | |
|ΔSCOPE 2| |0.463***| |0.438***| | |
| | |(0.117)| |(0.112)| | |
|ΔSCOPE 3| | |1.480***| |1.456***| |
| | | |(0.321)| |(0.322)| |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|135,522|135,570|135,594|135,522|135,570|135,594|
|R-squared|0.230|0.230|0.230|0.233|0.233|0.233|

# Panel C: Emission intensity

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|SCOPE 1 INT|0.004| | |-0.012| | |
| |(0.016)| | |(0.016)| | |
|SCOPE 2 INT| |0.154| |0.150| | |

# Table 13

# Carbon emissions and institutional ownership: excluding salient industries.

The sample excludes companies in the oil & gas (gic=2), utilities (gic=65-69), and transportation (gic=18, 19, 23) industries. The sample period is 2005-2017. Panel A presents the results for aggregate ownership for contemporaneous carbon intensity measures, Panel B for disaggregated ownership. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the industry and year level (in parentheses). All regressions include year-month fixed effects. In Panel A, the regressions for columns 2, 4, and 6, the regressions additionally include state-fixed effects. All regressions for Panel B results include state fixed effects. ***1%; **5%; *10% significance.

# Panel A: Aggregate ownership

|Variables|(1)| |(2)| |(3)| |(4)|(5)|(6)|
|---|---|---|---|---|---|---|---|---|---|
|SCOPE 1 INT|-0.015| |-0.007| | | | | | |
| |(0.094)| |(0.104)| | | | | | |
|SCOPE 2 INT| | | | |-0.565| |-0.525| | |
| | | | | |(1.968)| |(2.024)| | |
|SCOPE 3 INT| | | | | | | |0.421|0.246|
| | | | | | | | |(0.538)|(0.568)|
|Controls| |Yes|Yes|Yes|Yes|Yes|Yes| | |
|Year/month F.E.| |Yes|Yes|Yes|Yes|Yes|Yes| | |
|State fixed effect|No| |Yes|No|Yes|No|Yes| | |
|Observations|152,799| |143,337|152,799|143,337|152,799|143,337| | |
|R-squared|0.126| |0.169|0.126|0.169| | |0.127|0.170|

# Panel B: Disaggregate ownership

| |(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
| | | | | | | |

# Table 14

# Carbon emissions and stock returns: sub-periods.

The sample period is 2005-2017. The dependent variable is RET. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the firm and year/month level (in parentheses). All regressions include year-month fixed effects and industry-fixed effects. We report the results for the natural logarithm of contemporaneous total emissions in Panel A; the results for the growth rate in firm emissions in Panel B; and the results for emission intensity in Panel C. ***1% significance; **5% significance; *10% significance.

# Panel A: Total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|LOG (SCOPE 1 TOT)|0.127***| | |0.205**| | |
| |(0.037)| | |(0.075)| | |
|LOG (SCOPE 2 TOT)| |0.127***| | |0.233**| |
| | |(0.042)| | |(0.087)| |
|LOG (SCOPE 3 TOT)| | | |0.265***| |0.340***|
| | | | |(0.086)| |(0.107)|
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|Yes|Yes|Yes|Yes|Yes|Yes|

# Panel B: Growth rate in total emissions

|Variables|(1)|(2)|(3)|(4)|(5)|(6)| |
|---|---|---|---|---|---|---|---|
|ΔSCOPE 1|0.610***| | |0.629**| | | |
| |(0.161)| | |(0.249)| | | |
|ΔSCOPE 2| |0.265***| | |0.459**| | |
| | |(0.097)| | |(0.193)| | |
|ΔSCOPE 3| | |1.259***| |1.032**| | |
| | | |(0.355)| |(0.436)| | |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes| |
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes| |
|Industry F.E.|Yes|Yes|Yes|Yes|Yes|Yes| |
|Observations|108,888|108,804|108,948|44,163|44,151|44,175| |
|R-squared|0.278|0.279|0.279|0.089|0.089|0.089| |

# Panel C: Emission intensity

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|SCOPE 1 INT|0.005| | |0.010| | |
| |(0.007)| | |(0.019)| | |
|SCOPE 2 INT| |0.091| |0.117| | |
| | |(0.094)| |(0.125)| | |
|SCOPE 3 INT| | |0.030| |0.040| |
| | | |(0.091)| | |(0.087)|
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Observations|121,778|121,778|121,778|62,606|62,606|62,606|
|R-squared|0.268|0.268|0.268|0.114|0.114|0.114|

# Table 15. Paris Agreement and stock returns: difference-in-differences estimation.

The dependent variable is RET. Our treatment sample is the subset of firms in the largest quartile of the distribution of firms sorted by the size of their carbon emission as of the end of 2014. We match these firms with a control group of firms with similar characteristics identified by the nearest neighbor method. The matching characteristics we use are the same as those in our return regressions. TREAT is a generic indicator variable taking the value one for firms in the treatment sample and zero for firms in the control sample, and AFTER is an indicator variable equal to zero for the period 2015/05-2015/11 and equal to one for the period 2015/12-2016/05. We estimate this model separately for each scope and emission measure. In the regressions, the sorts correspond to each scope measure which then separately identify each individual treatment variable. We also include firm and year-month fixed effects in the regression. All variables are defined in Table 1. Standard errors (in parentheses) are clustered at the firm and year/month level. All regressions for columns 4-6 include industry-fixed effects. We report the results for the natural logarithm of contemporaneous total emissions in Panel A; the results for the growth rate in firm emissions in Panel B; and the results for emission intensity in Panel C. ***1% significance; **5% significance; *10% significance.

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|Panel A: Total emissions|TREAT1*AFTER|10.615***| |10.705***| | |
| |(1.175)| | |(1.200)| | |
| |TREAT2*AFTER| |-1.783| |-1.681| |
| | |(5.861)| | |(5.821)| |
| |TREAT3*AFTER| | |-8.917| |-8.782|
| | | |(6.081)| |(6.127)| |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Firm F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|5,452|6,604|6,604|5,452|6,604|6,324|

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|Panel B: Growth rate in total emissions|TREAT1*AFTER|0.438| |4.425| | |
| |(4.426)| | |(3.373)| | |
| |TREAT2*AFTER| |-3.712| |0.361| |
| | |(3.541)| | |(2.592)| |
| |TREAT3*AFTER| | |0.396| |3.671|
| | | |(4.338)| |(3.927)| |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Firm F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|5,764|5,706|5,901|5,764|5,706|5,901|

# Panel C: Emission intensity

|TREAT1*AFTER|2.825|2.855|
|---|---|---|
| |(5.876)|(5.994)|
|TREAT2*AFTER|-0.016|0.021|
| |(5.344)|(5.417)|
|TREAT3*AFTER|-7.614***|-7.749***|
| |(2.070)|(2.128)|

|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|---|---|---|---|---|---|---|
|Firm F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|4,540|4,853|4,736|4,540|4,853|4,736|

Table 16. Carbon emissions and stock returns (imputed emissions). The sample period is 1990-1999. The dependent variable is RET. All variables are defined in Table 1. We report the results of the pooled regression with standard errors clustered at the firm and year level (in parentheses). All regressions include year-month fixed effects. In the regressions for columns 4 through 6, we additionally include industry-fixed effects. The total level of emissions is imputed using the earliest observed level of emission intensity for each firm for the period 2005-2017 (in Panel A) and for 1990-1999 (in Panel B) and scaling it by respective revenue values. ***1% significance; **5% significance; *10% significance.

# Panel A: (2005-2017)

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|LOG (SCOPE 1 TOT)|0.097***| | |0.291***| | |
| |(0.024)| | |(0.046)| | |
|LOG (SCOPE 2 TOT)| | |0.186***| |0.336***| |
| | | |(0.043)| |(0.065)| |
|LOG (SCOPE 3 TOT)| | | |0.245***| |0.585***|
| | | | |(0.043)| |(0.127)|

|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|---|---|---|---|---|---|---|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|161,122|161,062|161,313|161,122|161,062|161,313|
|R-squared|0.199|0.200|0.200|0.203|0.203|0.204|

# Panel B: (1990-1999)

|LOG (SCOPE 1 TOT)|-0.037| | |0.082| | |
|---|---|---|---|---|---|---|
| |(0.034)| | |(0.078)| | |
|LOG (SCOPE 2 TOT)| |0.033| |0.236| | |
| | |(0.045)| |(0.134)| | |
|LOG (SCOPE 3 TOT)| | |0.005| |0.318*| |
| | | |(0.059)| |(0.162)| |
|Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|Year/month F.E.|Yes|Yes|Yes|Yes|Yes|Yes|
|Industry F.E.|No|No|No|Yes|Yes|Yes|
|Observations|59,878|59,878|59,878|59,878|59,878|59,878|
|R-squared|0.149|0.149|0.149|0.156|0.156|0.156|