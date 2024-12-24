# No 418

# APRIL 2020/rev

# CefeD

# Center for European Studies

# PAPER SERIES

# The Greenium matters: greenhouse gas emissions, environmental disclosures, and stock prices

# Lucia Alessi, Elisa Ossola and Roberto Panzica

The Center for European Studies (CefES-DEMS) gathers scholars from different fields in Economics and Political Sciences with the objective of contributing to the empirical and theoretical debate on Europe:

# DEGLI STUDI DIPARTIMENTO DI ECONOMIA; METODI QUANTITATIVI E STRATEGIA DI IMPRESA

Electronic copy available at: https://ssrn.com/abstract=3452649

Bicocc 8

# The Greenium matters: greenhouse gas emissions, environmental disclosures, and stock prices

# Lucia Alessi1,2, Elisa Ossola1, and Roberto Panzica1

# 1European Commission, Joint Research Centre

# 2CefES – Center for European Studies (Università degli Studi di Milano-Bicocca)

# April 2020

# Abstract

This study provides evidence on the existence of a negative Greenium, i.e. a risk premium linked to firms’ greenness and environmental transparency, based on European individual stock returns. We define a priced ‘greenness and transparency’ factor based on companies’ greenhouse gas emissions and the quality of their environmental disclosures. Based on this factor, we offer a tool to assess the exposure of a portfolio to the risk associated with the low-carbon transition, and hedge against it. We estimate that in a stressed scenario where greener and more transparent firms very much outperform brown stocks, there would be losses at the global level, including for European large banks, should investors fail to price climate-transition risks. These results call for the introduction of climate stress tests for systemically important financial institutions.

# Keywords

Climate risk, environmental disclosure, factor models, asset pricing, stress test.

# J.E.L. classification

G01; G11; G12; Q01.

∗Disclaimer: The content of this article does not necessarily reflect the official opinion of the European Commission. Responsibility for the information and views expressed therein lies entirely with the authors. This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors. We thank the co-editors and two anonymous referees for constructive criticism and numerous suggestions which have lead to substantial improvements over the previous versions. We thank the authors of Battiston et al. (2017) for providing us with their data, which we use for the climate stress test. We are grateful to Ivan Faiella for his comments on the construction of the greenness and transparency indicator. We thank participants at a number of conferences, including CefES, IRMC, Finance for Sustainability, CREDIT, EAEPE, as well as at meetings and workshops at the European Central Bank, and seminars at the Universidad Autonoma de Madrid and the EC Joint Research Centre, for useful suggestions. E-mail: lucia.alessi@ec.europa.eu, elisa.ossola@ec.europa.eu, roberto.panzica@ec.europa.eu.

1 Electronic copy available at: https://ssrn.com/abstract=3452649

# 1 Introduction

Climate change is a fact, but we are not sure what the economic costs associated with this change will be.1 By the same token, it is difficult to estimate what the economic benefits of doing something about it would be. In particular, it would be hard to pin down the net present value of activities aimed at climate change adaptation and mitigation, as well as those directed to broader environmental objectives such as the sustainable use and protection of water and marine resources, the transition to a circular economy, waste prevention and recycling, pollution prevention and control, and the protection of healthy ecosystems.2 At the same time, the consequences of a transition to a low-carbon, resource-efficient and circular economy, or lack thereof, are also largely uncertain. Hence, these issues have to be addressed as aspects of long-run risk. The contribution of this paper is to measure the added value of greener economic activities in terms of market excess returns. To do so, we first show that indeed, the European market prices climate risk in the form of a greenness and environmental transparency factor, in the context of a standard asset pricing model. Second, we estimate that the market associates a negative risk premium, which we label Greenium, to more environmentally friendly and transparent firms.

We identify the greenness and transparency factor based on a precise definition. In particular, we first construct portfolios characterized by a different shade of green and a different degree of environmental transparency. This is based on firm-level information on greenhouse gas (GHG) or CO2 emissions, combined with a measure of the completeness of firms’ environmental disclosures, to yield a synthetic greenness and transparency index for each stock. Companies which disclose a lower emission intensity, and are very transparent, attain the highest scores and are included in a greener and more transparent portfolio. The most straightforward example of greener companies would be those with a large share of their turnover in green economic sectors, e.g. renewable energy. Conversely, companies which do not disclose information on their environmental performance are labeled as non-transparent. Among these nontransparent companies, those active in carbon-intensive sectors, e.g. companies operating coal power plants, are included in a brown portfolio. The greenness and transparency factor is constructed based on 942 companies listed on the STOXX Europe Total Market Index.

By relying on company-level disclosures and factoring-in their transparency, we try to tackle the issue of green-washing, which is likely to be the reason why the literature has so far failed to find a consensus on the existence of a priced green factor. Indeed, looking at the actual composition of the portfolios of publicly traded investment funds which label themselves as ‘green’ or ‘sustainable’, it turns out that many funds are clearly less environmentally friendly than their name would suggest. For example, a fund might indeed limit its exposure to carbon-intensive sectors, but at the same time mainly invest in e.g. financial stocks. Banks, insurers and other financial institutions are admittedly directly responsible for a very small fraction of GHG emissions, but financial institutions are prob-

1 On the uncertainty on the rate of increase in average temperatures in the long-medium horizon, and on the effects of climate change, see e.g. Pindyck (2013). 2 These objectives are listed in the European Commission Action plan on financing sustainable growth, which sets out an EU strategy for sustainable finance.

ably not what comes to mind when thinking of companies that are at the forefront of efforts to reduce emissions. At the level of the individual company, there could be a tendency to disclose only partial information, emphasizing the environmental dimensions where the firm performs best and neglecting those where the firm does not as well. For example, a car manufacturer may report its scope 1 GHG emissions, i.e. emissions from sources that it owns or controls, but could have an incentive not to disclose its scope 3 emissions, which include emissions resulting from the use of the vehicles it produces and sells. By considering the completeness of the relevant information that firms disclose, we deal with this type of greenwashing.

At the same time, however, one should be careful not to take extreme views when defining ‘green’ stocks. As a matter of fact, portfolio diversification is crucial for asset managers, and concentrating the exposure on a small set of pure green players is not a viable option. Our society will still need e.g. steel and cement for quite a while, and companies’ low-carbon transition is a much needed but gradual process. For all these reasons, a sensible approach would be to broaden the scope of the definition of ‘green’ beyond pure players to also include firms that meet the highest level of energy efficiency and the lowest CO2 emissions within the relevant sector. By taking this approach, a steel manufacturer which also uses scrap steel is greener than one that does not. By the same token, an energy company that reduces its reliance on fossil fuels – though not having an entirely renewable energy mix – is greener than one that is not reducing its carbon footprint. This is the approach taken by several providers of environmental ratings, which assess the sustainability of firms relative to their peers, and also the one we take in this paper.

We show that in the context of a standard asset pricing model, the portfolios we build based on firms’ environmental performance and disclosures are associated with a positive intercept, suggesting the existence of an omitted factor. Based on this evidence, we propose to include a greenness and transparency factor, which we construct based on a long-short strategy involving the greener and more transparent portfolio and the brown portfolio. We find that the Greenium, i.e. the risk premium associated with this greenness and transparency factor, is negative and highly statistically significant. This means that investors accept a lower remuneration for their investments, ceteris paribus, insofar as these investments are linked to greener and more transparent firms. We interpret this as evidence of climate risk being viewed as significant, with the market seeing value in investing in greener assets as a hedging strategy towards worse environmental outcomes.

Indeed, in a scenario of heightened risks resulting from climate change, there would be a stronger push towards more environmentally friendly activities, with more decisive political action likely to be taken to promote sustainable growth. Hence, companies active in green sectors and more transparent on their environmental performance would operate in a more favorable environment, possibly supported by incentives, e.g. fiscal or of other nature. At the same time, the likelihood would increase that some assets, e.g. coal, would become stranded. In this context, forward-looking investors who base their portfolio allocation on a broader information set than past returns, invest in greener assets already today.

The evidence we provide on the existence of a Greenium has clear financial stability implications. Indeed, we show that the European market as a whole does price climate risk. In this context, if an investor does not factor in

3

Electronic copy available at: https://ssrn.com/abstract=3452649

Climate risk in the construction of her portfolio, she is in fact pricing her holdings based on a misspecified model, where the greenness and environmental transparency factor is omitted. Should this mispricing affect the assets held by systemically important financial institutions (SIFIs) such as large banks, insurers and pension funds, there could be consequences in terms of systemic risk. In particular, asset returns on their holdings could be negatively affected by climate change via two main channels. First, in a longer horizon perspective, more frequent and severe natural catastrophes stemming from climate change (e.g. typhoons and floods) could negatively affect returns on assets linked to particularly vulnerable economic activities. These are the so-called physical risks related to climate change, that we do not tackle in this paper directly. However, it has been shown that rising temperatures have strong adverse effects on asset valuations, as well as on key macroeconomic aggregates and productivity (see Donadelli et al., 2017). Second, in a medium-term perspective, the implementation of sustainable finance policies will imply higher costs for firms with higher emissions, causing a generalized drop in the dividend that brown firms will be able to pay to their shareholders. In parallel, carbon-intensive assets will increasingly become ‘stranded’ (see Campiglio et al., 2017). This is the so-called transition risk. These two channels characterize a climate risk factor that investors should price.

Based on our model, we estimate that in an extreme but plausible scenario where greener and more transparent companies outperform brown companies, all institutional sectors at the global level, including e.g. governments, non-financial institutions and financial corporations, as well as all European SIFIs, would be hit by losses. By halving their exposure to carbon-intensive sectors and reallocating their investments towards greener assets, investors could somewhat reduce the loss. However, they could only avoid losing money if they would reallocate their investments towards greener and more transparent firms. The magnitude of the expected losses we estimate is admittedly not breathtaking. Still, we show that no one is in a safe place when it comes to climate risk, as the consequences of brown asset mispricing would be widespread. Moreover, our analysis is limited to equity holdings, that for some investors are not as relevant as other types of exposures. In a stressed scenario, however, losses would almost certainly be recorded also on the bond portfolio and notably, on banks’ loan exposure. Finally, we use a simple model to compute losses, based on the marginal expected shortfall. This approach does not factor in losses resulting from second-round effects, like fire sales, which could magnify first-round losses. Taking all this into account, we conclude that a climate or climate-policy shock could have serious implications in terms of financial stability, especially if coupled with shocks of other nature. Hence, we argue that a climate stress test is warranted for systemically important institutions to monitor their resilience to climate change. The greenness and transparency factor we construct could indeed be used by investors, to hedge against climate risk, and by supervisors, to measure SIFIs exposure to this risk. Notice that looking ahead, we can only expect greater policy pressure to reducing carbon.

3See Daniel et al. (2016).

Electronic copy available at: https://ssrn.com/abstract=3452649

# emissions and moving to a sustainable development path.

The paper is structured as follows. In the next section, we provide an overview of the relevant literature. In Section 3, we present our synthetic greenness and transparency indicator at the level of the individual company. Section 4 outlines the asset pricing theoretical framework. In Section 5, we present the results of the empirical application. First, we focus on portfolios by estimating the standard asset pricing models and defining the greenness and transparency factor. Then, we estimate our proposed model on individual stocks. In Section 6 we carry out a battery of robustness checks. Section 7 tests the performance of the equity portfolios of global institutional sectors and European SIFIs in a climate-stressed scenario. Section 8 concludes.

# 2 Related literature

This paper stands at the crossroad of sustainable finance, asset pricing and financial stability. The sustainable finance literature has so far mostly focused on corporate performance, starting from the seminal work by Bragdon and Marlin (1972). They asked the fundamental question, whether there would be a reward for a company’s virtue. Trying to answer this question, Porter (1991), Gore (1993), and Porter and van der Linde (1995) argue that improving a company environmental performance can lead to a better economic or financial performance, not necessarily accompanied by an increase in costs. Ambec and Lanoie (2008) review several empirical works showing that improvements in the environmental performance of a firm tend to be associated with improvements in its economic or financial performance, owing to potential revenue increases and/or cost cuts. More recently, Hoepner et al. (2018) show that engagement on sustainability issues can benefit shareholders’ by reducing firms’ downside risks.

Despite increasingly available evidence on the performance of green or sustainable corporates, however, no consensus has yet been reached in the asset pricing literature about the performance of green assets, or on environmental risk being a priced macro factor. Evidence based on a large number of studies on the performance of sustainable investment funds compared with conventional peers (e.g., Statman, 2000; Renneboog et al., 2007; Seitz, 2010) is mixed. For example, Hartzmark and Sussman (2019) find that sustainability is viewed as positively predicting future performance; however, they do not find evidence of outperformance of ‘high sustainability’ investment funds vs ‘low sustainability’ ones. Trinks et al. (2018) show that divesting from fossil fuels does not impair portfolio performance. On the contrary, Bolton and Kacperczyk (2019) find that stocks of companies with higher CO2 emission intensity earn higher returns. Other analyses based on publicly traded environmental portfolios find that green stocks are, on average, underperforming the market. This finding would indicate that investors are willing to earn comparatively less on these assets because they are hedging an environmental long-run risk. Finally, recent papers attempt to build climate risk hedging portfolios (see Engle et al., 2020, Choi et al., 2020, Hong et al., 2019, Alok).

Andersson et al. (2016) shows that divestment in higher emission stocks entails a cost, which investors are more likely to bear the stronger the perception of a serious commitment on the side of policymakers towards fighting climate change.

et al., 2020 and Goergen et al., 2019, Monasterolo and De Angelis, 2020); however, none of these works goes all the way to quantifying the associated risk premium.

Finally, the financial stability literature has started to put forward the idea of ‘climate stress tests’ on the exposures of financial institutions (see Battiston et al., 2017 and Battiston and Monasterolo, 2018), as well as to develop climate stress-test methodologies for e.g. loan portfolios (see Monasterolo et al., 2018). Central Banks and international institutions, starting with the seminal speech by Carney (2015), have also emphasized on different occasions that climate change could affect systemic risk. In particular, Gros et al. (2016) distinguishes between a benign scenario, with a gradual transition to a low-carbon economy, and an adverse scenario, where the transition occurs more abruptly. In both cases, there could be financial stability consequences: with a too slow transition, the Paris Agreement goal would be missed and the catastrophic consequences of climate change would become unavoidable.5 A too quick transition, on the other hand, would imply a sudden repricing of brown assets. We provide evidence that these concerns are shared by the market.

# 3 Synthetic greenness and transparency indicator

Different indicators are available to assess a company’s commitment to the environment. However, identifying synthetic proxies for firms’ environmental performance is not obvious and no consensus has yet been reached in the literature on this issue (see Oikonomou et al., 2012). The main source of information in this respect are firms’ environmental disclosures, which are typically published by companies in their annual reports, or in separate Corporate Social Responsibility or Sustainability reports, as well as in dedicated ESG releases or Corporate Governance reports. Based on these disclosures, investors distinguish companies that are doing green business from firms that are not, or that are not transparent in this respect. However, a single indicator might not be sufficient to ensure a careful assessment of a company’s environmental performance. Hence, we look at both of the following two dimensions: i) environmental transparency, related to the quality of firms’ environmental disclosures, and ii) GHG emissions.

As a proxy for the environmental transparency of a company we use the Bloomberg Environmental disclosure score, which we refer to as E score.6 This is an index quantifying the completeness of a firm’s disclosure on its impact on the environment. The E score embraces several environmental aspects of a firm’s business. In particular, it looks at how transparent a company is with respect to its carbon emissions, air and water pollution, its commitment to the protection of biodiversity, and its waste management, among others. The weighted E score is normalized to range from zero for companies that do not disclose environmental data to 100 for those which disclose detailed information for each pillar. The score is also tailored for industry sectors, and each component is weighted based on its importance. In particular, GHG emission disclosure is attached the highest weight.

5 The objective of the Paris Agreement, signed in 2015, is to keep a global temperature rise this century well below 2 degrees Celsius above pre-industrial levels and to pursue efforts to limit the temperature increase even further to 1.5 degrees Celsius.

6 MSCI, RobecoSAM, Sustainalytics and Asset4 also provide E disclosure scores based on different methodologies.

Electronic copy available at: https://ssrn.com/abstract=3452649

We use the E score as a measure of the transparency of a firm with respect to its environmental sustainability commitment, and assume that higher commitment is associated with higher transparency. In other words, based on the E score, we make a first selection among firms that are transparent, at least to some extent, about their environmental performance, and firms that are not. We do not claim that firms that do not disclose information on environmental issues are necessarily ecologically destructive. However, we find it legitimate to label them as non-green, as their environmental commitment appears weaker compared to firms that do disclose (quantitative) information on this pillar. Moreover, Marquis et al. (2016) show that more environmentally friendly firms tend to disclose more because they know that their environmental performance is generally better than the one of their peers, while more environmentally damaging firms are indeed less likely to engage in non-mandatory disclosure, in particular in those countries where they are more exposed to scrutiny and norms.

To build a comprehensive index of a company’s environmental performance, we combine this transparency measure with quantitative disclosure on emissions. In particular, we consider the total GHG emission intensity, i.e. the total amount on GHG emissions normalized by revenues. If this is not available, we take the total carbon dioxide (CO2) emitted, weighted by revenues. The synthetic greenness and transparency indicator Gi,y of company i at year y is defined as the weighted average of the two components, as follows:

Gi,y = γKi,y + (1 − γ)Ei,y , with γ ∈ [0, 1],

(1)

where Ki,y is the inverse of the ranking of firm i in term of emission intensity, and Ei,y is the ranking of firm i in term of E score. The parameter γ controls for the relative importance of the two components of the index. We set γ = 0.5 as benchmark case, and show results for γ = 0.2 and γ = 0.8 as robustness checks in Section 6. More transparent companies, for a given level of intensity of GHG or CO2 emissions, are associated with larger values of the indicator Gi,y. Firms that attain a lower emission intensity, for a given level of transparency, are also associated with larger values of Gi,y.

Figure 1 shows the number of companies in our sample which did some environmental disclosure, from 2005 to 2017 (yellow bar). The figure also reports the number of firms that disclosed their emission intensity in a given year (gray bar). The number of companies reporting on their environmental performance has exhibited an upward trend in the last ten years, reaching around 700 EUROSTOXX companies in 2017, i.e. more than half of the sample.

The indicators we use to build the synthetic greenness and transparency indicator have some limitations. First, the analysis provided in Section 5 includes data from 2005, while the Bloomberg ESG application was launched only in 2009. This potentially introduces look-ahead bias (see, e.g., Derwall et al., 2005). However, this bias is mitigated by the availability of firms’ environmental disclosures, including on GHG emissions, also prior to 2009. In other words, market participants could start using the Bloomberg E score as such only as of 2009, but the information.

Figures 2 and 3 in the Appendix plot the greenness and transparency indicator, as well as its components, for two representative companies.

Electronic copy available at: https://ssrn.com/abstract=3452649

# Figure 1: Total number of companies for which E score (yellow bar) and emission intensity (gray bar) are available.

| |2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |900| | | | | | | | | | | | | |
| |800| | | | | | | | | | | | | |
| |700| | | | | | | | | | | | | |
| |600| | | | | | | | | | | | | |
| |500| | | | | | | | | | | | | |
| |400| | | | | | | | | | | | | |
| |300| | | | | | | | | | | | | |
| |200| | | | | | | | | | | | | |
| |100| | | | | | | | | | | | | |
| |0| | | | | | | | | | | | | |

This index is based on was already available to the market. A second issue relates to the self-reported nature of GHG emissions, as well as of other environmental disclosures. As a matter of fact, the EU Non-Financial Reporting Directive (NFRD) only requires auditors to verify the publication of non-financial disclosures by relevant firms, but there are no assessment and verification requirements on the content of non-financial disclosures. Based on this, we should emphasize that those firms we identify as greener based on their environmental disclosures may actually be less green than they claim. Still, our asset pricing analysis should not be affected by this problem, insofar as investors base their decisions only on publicly available information as we do. Related to the issue of self-reporting is that of self-selection, due to the fact that unless firms are subject to the NFRD, they are free to choose whether to disclose environmental information. Those that are subject to the NFRD, can choose what to disclose in particular. Typically, self-selection may introduce a bias in the analysis. However, in our case self-selection works in the right direction, as greener firms have an incentive to disclose more and in our framework, firms that are characterized by a lower emission intensity and better environmental disclosures are correctly identified as greener and more transparent. Still, we miss information on those firms that do not disclose. Finally, ESG ratings may differ quite substantially across different data providers, as shown by a growing stream of empirical literature, including, among others, Chatterji et al. (2016), Escrig-Olmedo et al. (2019), and Berg et al. (2019). This latter paper, for example, shows that there is much more disagreement among raters on environmental ratings compared to credit ratings, but still less compared to social and governance ratings. To partly account for the limited reliability of environmental ratings and scores, we use the E score in combination with quantitative data on carbon emissions. We also show Performing the analysis from January 2010 to August 2018 yields empirical results in line with the ones provided in Section 5. See Directive 2014/95/EU. On this point, Short and Toffel (2008) document that firms tend to disclose more when they are immune from prosecution for self-disclosed violations.

Electronic copy available at: https://ssrn.com/abstract=3452649

that using only one or the other component of the greenness and transparency indicator does not yield meaningful results (see Section 6).

Finally, among non-transparent firms, we further select a subsample that we label ‘brown’. These are companies which are mainly active in sectors characterized by a comparatively higher level of carbon emissions. Information on sectoral emissions in Europe is provided by Eurostat, at the NACE-2 digit level.10 Table 9 in the Appendix lists the economic sectors responsible for the largest amount of carbon emissions in the EU. Overall, these sectors account for 85% of the total GHG emissions in the EU over the 2008-2017 period. Table 10 in the Appendix lists the companies that are included in the brown portfolio in 2017.

# 4 Linear factor model

We assume an approximate factor structure for excess returns combined with the absence of arbitrage opportunities to obtain asset pricing restrictions. As the greenness and transparency indicator defined in Equation (1) is only available for a relatively short sample, we opt for a time-invariant model, which assumes that the exposition of an asset i to each observable factor does not evolve over time. We acknowledge that a model that accounts for time variation in parameters and hence in risk premia would be best suited in this context, owing to the fact that awareness on climate issues has increased over time. However, a time-varying model for the excess returns could only be estimated on a much longer time series and a much larger cross-section than ours. Indeed, it would imply introducing functional specifications for the coefficients, which would result in an incidental parameter problem.

Let us define the excess return on asset i = 1, ..., n at time t = 1, 2, ...T as Ri,t = ri,t − rf,t, where ri,t is the log-return and rf,t is the risk-free return. We assume that the excess return Ri,t satisfies the following linear factor model:

Ri,t = ai + ∑k=1Kbi,kft,k + εi,t,K (2)

where ft,k is the k-th observable factor, with k = 1, ..., K. The error term εi,t is such that E[εi,t|Ft−1] = 0, and Cov[εi,t, ft|Ft−1] = 0, where Ft−1 is the lagged information set. The approximate factor structure holds for the variance-covariance of the error terms, i.e., Σε,t,n = [Cov[εi,t, εj,t|Ft−1]]i,j=1,...,n with bounded largest eigenvalue (see, e.g., Chamberlain and Rothschild, 1983). The following parameter restriction holds:11

ai = ∑k=1Kbi,kνk (3)

where νk is a parameter defined for each k-th factor. The asset pricing restriction in Equation (3) can be rewritten as the usual linear relation between expected excess returns and risk premia:

Source: https://ec.europa.eu/eurostat/data/database.

We refer to Gagliardini et al. (2016) for theoretical results and proofs.

Electronic copy available at: https://ssrn.com/abstract=3452649

E[Ri,t] = ∑bi,kλk.K (4)

Based on Equations (3) and (4), the time-invariant risk premium associated to each k-th factor is the following:

λk = E[ft,k] + νk. (5)

The risk premium λk is the sum of the expected return on the factor, which can be estimated as its first moment, plus the parameter νk, defined in the asset pricing restriction (3). Risk premia measure how much investors are willing to pay to hedge the systematic risk captured by the observable factors. When the factors are asset returns themselves (i.e., factors are tradable) and are assumed to be priced by the same model in (2), the risk premia are equal to the factor means (see, e.g., Jagannathan and Wang, 2002). However, if factors are non tradable, the parameter νk is non zero. Following Gagliardini et al. (2016), we do not assume a priori that the factors ft,k are tradable. Hence, we allow for the existence of market imperfections, such as transactions costs due to rebalancing and short selling, which are captured by ν (see e.g., Cremers et al., 2012).

Our baseline factor models are summarized in the table below.

|Model|Reference|Abbreviation|Factors|K|
|---|---|---|---|---|
|Four-factor model|Carhart (1997)|CAR|fm,t, fsmb,t, fhml,t, fmom,t|4|
|Three-factor model|Fama and French (1993)|3FF|fm,t, fsmb,t, fhml,t|3|
|Capital Asset Pricing Model|Sharpe (1964); Lintner (1965)|CAPM|fm,t|1|

The factors that are included in the models are the following: 1) fm,t is the market factor, defined as the excess return on the European value-weighted market portfolio over the risk free rate; 2) fsmb,t is the size factor, defined as the average return on small caps minus the average return on big caps; 3) fhml,t is the book-to-market factor, defined as the average return on the value portfolio (i.e. stocks that have market value that is small relative to the book value) minus the average return on the growth portfolio; 4) fmom,t is the momentum factor, defined as the average of the returns for the winner portfolio, based on past returns, minus the average of the returns for the loser portfolio. Fama and French (2015) propose a five-factor model including the three Fama-French factors plus profitability and investment factors. However, we do not consider the five-factor model as four factors are enough to explain excess returns in a time-invariant specification, as shown by Gagliardini et al. (2019). By analogy with the fm,t factor, which is constructed based on the T-bill, we proxy the risk free rate with the 30-day T-bill beginning-of-month yield. The time series of European factors and the risk free rate are available on Kenneth French’s website.

10 Electronic copy available at: https://ssrn.com/abstract=3452649

# 5 Empirical analysis

In this section, we first compare greener and more transparent portfolio and the brown portfolio based on the models introduced in the previous section. Then, we propose an observable greenness and transparency factor defined as the difference between the returns on the greener and more transparent portfolio and those on the brown portfolio. Finally, we estimate the Greenium, i.e. the risk premium associated to the greenness and transparency factor, using a set of European individual stocks. Our sample spans from January 2006 to August 2018, covering all individual stocks included in the STOXX Europe Total Market Index (TMI) on August 2018.12 The STOXX Europe TMI covers approximately 95% of the free float market capitalization across 17 European countries.13 In principle, we could estimate our model on all 20K European listed firms. However, enlarging the sample would only marginally increase its coverage in terms of market capitalization, while it may jeopardize the results owing to the quality of the information that we would feed into the model. Indeed, the reliability of the data we use for our application crucially depends on the quality of environmental disclosures of European firms. On this matter, the NFRD imposes mandatory disclosures only on larger firms (with more than 500 employees). To be on the safe side, we construct our greenness and transparency factor based on a sample which is more reliable in terms of data quality, insofar as it is based on a market index, and still representative of the market as a whole. We present an application on a much larger sample in Section 6.

As in Fama and French (2008), we exclude financial firms (i.e., companies classified in sectors with NACE code K or L). The final dataset comprises n = 942 stocks. Stock returns and stock market capitalization data are sourced from Bloomberg. The panel is unbalanced, i.e., asset returns are not available for all firms at all dates. To account for publication lags, in each given year we use environmental disclosures for the previous reference year.

# 5.1 Portfolio analysis and the Greenness and Transparency Factor

As described in Section 3, we distinguish between transparent and non-transparent companies. The former belong to set T while the latter belong to set Tc. At each month t, we define the returns on the transparent and non-transparent portfolios, i.e. ˜t and ˜c, respectively, as follows:

rt

˜t = ∑i∈Twiri,t,

˜c = ∑i∈Tcwiri,t,

where the weight is defined as wi = MCi,t/ ∑MCi,t, with MCi,t being the market capitalization of stock i at month t.

Focusing on transparent firms, we study the returns on different portfolios characterized by different shades of green and degrees of transparency. In particular, we build portfolios of returns ˜q corresponding to the quintiles q = 1, ..., 5 of the distribution of the greenness and transparency indicator considering only firms belonging to the set T.

12This allows us to avoid survivor bias in the data.

13These are Austria, Belgium, Czech Republic, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, the Netherlands, Norway, Portugal, Spain, Sweden, Switzerland, and the United Kingdom.

The portfolio built on the fifth quintile includes top-ranked firms in terms of environmental performance and disclosures and is labeled ‘greener and more transparent’ portfolio. The returns on this portfolio are indicated as rt ˜g.

Focussing on non-transparent firms, we build the brown portfolio by including companies in Tc which are active in one or more of the industries characterized by the highest emissions, as described in Section 3. The returns on this portfolio are indicated as ˜b. Table 12 in the Appendix reports descriptive statistics for firms included in portfolios characterized by various shades of green and transparency. It shows that the various portfolios are comparable in terms of average size of the companies and firms’ leverage, while firms in the non-transparent and brown portfolio tend to have a slightly better RoA compared to greener and more transparent firms.

# 1. Descriptive Statistics for Returns

Table 1 reports descriptive statistics for the returns on various portfolios, namely the one including all transparent firms ˜R, the greener and more transparent portfolio ˜Rg, the portfolio including all non-transparent firms ˜Rc, and the brown portfolio ˜b. With respect to the relative performance of the various types of firms, and looking at the mean return, the non-transparent portfolio has outperformed the others, followed by the brown and the transparent.

A sounder way to assess the performance of a portfolio is the Sharpe ratio, which relates the mean performance to the standard deviation of the returns on a portfolio. In terms of Sharpe ratio, the non-transparent portfolio still outperforms the others, which have a similarly better performance than the market. Neither the mean return nor the Sharpe ratio are monotone in greenness and transparency, which is explained by the fact that the environmental characterization of a portfolio is only one of the determinants of its performance (see below). Finally, the distribution of returns for all the portfolios is characterized by excess kurtosis and negative skewness.

# Table 1: Descriptive Statistics for Returns

|Portfolio|Mean|Std|Kurt|Skew|Sharpe|t-stat|
|---|---|---|---|---|---|---|
|˜R|1.102|0.497|3.744|-0.391|0.204|2.522|
|˜Rg|0.943|0.502|4.097|-0.593|0.188|2.315|
|˜Rc|1.732|0.586|5.210|-0.632|0.296|3.643|
|˜b|1.425|0.638|6.985|-0.909|0.224|2.754|

Taking a closer look at transparent firms, Table 13 in the Appendix reports descriptive statistics for quintile.

In the asset pricing literature there is no univocal choice on which percentiles of the distribution one should use for the construction of the relevant portfolios. For example, Ang et al. (2006) use quintiles, Baker and Wurgler (2006) use deciles, and Ahern (2013) use terciles. In general, the choice of the relevant percentiles is the result of a trade-off between the need to maximize heterogeneity between the two portfolios, and the need to ensure a large enough portfolio size. In our case, the top decile selects only a small number of stocks (as low as 13 in 2005), while terciles fail to identify the top firms in terms of environmental performance and transparency. Robustness checks using deciles and terciles are presented in Table 11 the Appendix.

Building portfolios based on the percentiles of the distribution of some relevant firm characteristic is standard in the asset pricing literature. It should be emphasized, however, that this is a relative approach to the classification of firms. In particular, a firm may cease to be included in the ‘greenest and more transparent’ portfolio if other firms reduce their emission intensity or improve their environmental disclosures, or if greener and/or more transparent firms are included in the sample, even if its environmental performance and transparency are unchanged in absolute terms.

Electronic copy available at: https://ssrn.com/abstract=3452649

portfolios 1-5, with portfolio R˜5 being the same as portfolio R˜g , i.e. the top green and transparent portfolio, while portfolio R˜1 includes comparatively higher emitting and less transparent firms, among those that do some environmental disclosure. Also in this case, the average return decreases as the level of the greenness and transparency indicator increases, though not monotonically (see Ciciretti et al., 2019 for a similar result based on an ESG characterization of firms). The same result holds when looking at the Sharpe ratio.

We investigate the drivers of the excess returns for the portfolios described above by considering the reference models described in Section 4. In particular, Table 2 reports the estimated factor loadings for the Cahart model (CAR), the three-factor Fama-French model (3FF), and the CAPM. Results are reported for the various portfolios. Overall, results are in line with the literature with respect to the market, size, value, and momentum factors, indicating that the portfolios we analyze are rather standard with respect to these dimensions. In particular, the estimated factor loading for the market factor bˆm is positive and significant across all models and portfolios. However, for the transparent as well as for the greener and more transparent portfolios, the exposition to the market factor is lower compared to the non-transparent and brown portfolios. This means that more transparent and greener firms tend to be less correlated with the market compared to more opaque and browner firms. The performance of the various portfolios can also be explained by the different loadings on the other factors. In particular, the exposition with respect to the size factor, bˆsmb, enters with a negative sign for the transparent and greener and more transparent portfolios, on the one hand, and a positive sign for the non-transparent and brown portfolios, on the other hand. This suggests that greener and transparent firms correlate more with bigger firms, while non-transparent and brown firms correlate more with smaller firms. Indeed, based on Table 12, firms in the greener and more transparent portfolio exhibit a slightly larger mean size as measured by total assets. As for the value factor ˆhml, the estimated loading is always negative and significant, except for the brown portfolio for which it is negative but non significant. Negative loadings on the value factor might mean that the portfolios include a comparatively larger share of firms with a lower book-to-market value. Considering the Carhart model, the coefficient on the momentum factor is not significant, except for the transparent portfolio. Looking at the explanatory power of the various models with respect to the different portfolios, the adjusted R-squared is lower for the brown portfolio based on all the models. Finally, the intercept is positive and significant for all portfolios and models, suggesting the existence of an omitted factor.

We define the greenness and transparency factor as the difference between the monthly returns on the greener and more transparent portfolio and those of the brown portfolio. Formally:

fg,t = ˜g− ˜.rt rb t

Table 3 reports the descriptive statistics of the Fama-French observable factors, the momentum and the greenness and transparency factor. The table includes also the cross-correlation structure among the factors. The greenness

Electronic copy available at: https://ssrn.com/abstract=3452649

# Table 2: Estimates of linear factor models on portfolio excess returns.

The table gathers results for transparent, green, non-transparent and brown portfolios considering the following linear models: four-factor Carhart model (CAR), three-factor Fama-French model (3FF) and the CAPM. Statistical significance at the 1% (***), 5% (**), and 10% (*) levels, and the adjusted R-squared (Radj).

| |Portfolio|R˜|Green|R˜c|Brown|
|---|---|---|---|---|---|
| |CAR model|CAR model|CAR model|CAR model|CAR model| | | | |
| |aˆ|0.005***|0.004***|0.011***|0.007***|
|ˆm|b|0.953***|0.945***|1.061***|1.112***|
|ˆsmb|b|-0.208***|-0.261***|0.476***|0.702***|
|ˆhml|b|-0.176***|-0.194***|-0.144**|-0.141|
|ˆmom|b|0.056***|0.046|-0.028|0.029|
| |R2adj|0.979|0.947|0.940|0.864|
| |3FF model|3FF model|3FF model|3FF model|3FF model| | | | |
| |aˆ|0.005***|0.005***|0.011***|0.008***|
|ˆm|b|0.944***|0.938***|1.065***|1.107***|
|ˆsmb|b|-0.213***|-0.264***|0.478***|0.700***|
|ˆhml|b|-0.212***|-0.224***|-0.126**|-0.159|
| |R2adj|0.978|0.947|0.940|0.865|
| |CAPM|CAPM|CAPM|CAPM|CAPM| | | | |
| |aˆ|0.006***|0.005***|0.012***|0.009***|
|ˆm|b|0.899***|0.891***|1.032***|1.063***|
| |R2adj|0.966|0.931|0.916|0.822|

and transparency factor is comparable to the other observable factors in terms of mean, standard deviation, kurtosis and skewness. It is also generally only mildly correlated with the other factors.

# Table 3: Descriptive statistics of the three Fama-French factors, momentum and greenness and transparency factors.

The table reports annualized mean return, standard deviation, kurtosis and skewness, as well as the factor correlation matrix.

|Factor|Mean|Std|Kurt|Skewn|fm|fsmb|fhml|fmom|
|---|---|---|---|---|---|---|---|---|
|fm|6.035|1.885|4.690|-0.642|1| | | |
|fsmb|1.671|0.641|3.195|-0.129|-0.034|1| | |
|fhml|-1.378|0.788|3.582|0.519|0.533|-0.062|1| |
|fmom|9.398|1.313|19.610|-2.546|-0.439|-0.009|-0.506|1|
|fg|-4.350|1.291|4.563|0.103|-0.224|-0.483|-0.206|0.268|

# 5.2 Asset pricing analysis

In this section we investigate whether the greenness and transparency factor defined in Equation (7) affects the cross-section of European stock returns. Further, we test whether investors accept lower (higher) compensation for holding environmentally friendly stocks by searching for a negative (positive) risk premium, i.e. a Greenium. The excess return Ri,t follows the model in Equations (2)-(3). In particular, we consider the same linear factor models used in the previous section, adding the greenness and transparency factor fg among the observable factors as follows:

Electronic copy available at: https://ssrn.com/abstract=3452649

|Model|Factors|K|
|---|---|---|
|CAR + G|fm,t, fsmb,t, fhml,t, fmom,t, fg,t|5|
|3FF + G|fm,t, fsmb,t, fhml,t, fg,t|4|
|CAPM + G|fm,t, fg,t|2|

The risk premium associated with the greenness and transparency factor is defined as follows:

λg = E[fg,t] + νg . (8)

In order to estimate the risk premia for the observable factors using individual stocks, we follow the estimation procedure proposed in Gagliardini et al. (2016). This procedure allows to deal with unbalanced panels, hence allowing to estimate the model on individual stocks rather than portfolios, and involves the following steps. First, we estimate the linear factor model by using the Ordinary Least Square (OLS) estimator. Second, we use the fitted residuals to test whether the model is correctly specified. In particular, we compute the diagnostic criterion proposed in Gagliardini et al. (2019), which checks whether the error terms share at least one unobserved common factor. Based on our sample, the criterion does not detect any common factor for the residuals, suggesting the validity of the factor structure.16 Third, we compute the cross-sectional estimator νk from (3) by Weighted Least Squares (WLS). Finally, the estimate of the risk premium ˆk for each factor is given by the sum of the expected λ return on the factor E[fk,t] and the estimate of ˆk.ν

Table 4 shows the estimated risk premia attached to the factors, including the Greenium, as well as the estimates for νk. Looking at the first two columns of the table, almost all risk premia are significant across the board, and have the expected signs. In particular, the estimated risk premia for the market, size, value and momentum factors are comparable with the results in Gagliardini et al. (2016) and Chaieb et al. (2018). The estimated Greenium is negative and significant at the 1% level in all cases. A negative Greenium indicates that investors accept lower compensation, ceteris paribus, to hold assets that correlate positively with the greenness and transparency factor, i.e. greener and more environmentally transparent assets. The mainstream interpretation of this result is based on the assumption that investors only care about their portfolios’ future payoffs. Hence, if they accept a lower remuneration to hold a certain type of assets, this must be because by doing so they are hedging some risks. In this specific case, holding greener and more transparent stocks constitutes a hedging strategy against climate risk. In the case of more environmentally friendly and transparent stocks, however, other considerations may also play a role. In particular, as suggested by Fama and French (2007), investors decisions may also be driven by some ‘taste for assets’, unrelated to expected returns. In this light, an emerging ‘taste for green’ in the market could also explain our result.

16For example, for the Carhart model plus the greenness and transparency factor, the difference between the largest eigenvalue of the empirical cross-sectional covariance matrix of the residuals ˆi,t and the penalization term is negative, pointing to the absence of ε omitted factors.

Electronic copy available at: https://ssrn.com/abstract=3452649

The last two columns of Table 4 refer to ˆk. Focussing on the greenness and transparency factor, ˆg is always ν negative and significant at the 1% level for the CAR+G, and at the 5% for the 3FF+G and CAPM+G models. For this component of the risk premium, the literature has proposed an interpretation linked to market imperfections (see, e.g. Daniel and Titman, 1997; Haugen and Baker, 1996). With reference to the Greenium, our hypothesis is that νg could capture alternative preferences of market participants, for example reflecting alternative expectations on future states of the economy (see Black and McMillan, 2006). In other words, some of the information that market participants have may not be fully captured based only on past returns. In this context, the difference between the investors’ larger information set and the smaller, backward-looking information set on which the model is estimated could be reflected in νk. This may be true in particular in the case of green and brown assets, in which case future perspectives may play a comparatively more important role than for other categories of assets.

# Table 4

The table reports the estimated annualized premia λˆk and the cross-sectional estimator ˆk for the factors ν in the Carhart model and for the greenness and transparency factor. The confidence intervals are reported at the 99% level. ***, ** and * denote significance at 1%, 5% and 10% levels, respectively.

| |CAR + G model| |3FF + G model| |CAPM + G|
|---|---|---|---|---|---|
|λˆm|10.659**|ˆm|10.534*|ˆm|11.137*|
|ν|4.625***| |4.499***| |5.102***|
| |(-4.913, 26.232)| |(-5.038, 26.106)| |(-4.435, 26.708)|
|λˆsmb|3.326**|ˆsmb|2.634|ˆsmb| |
|ν|1.655***| |0.963***| | |
| |(-1.354, 8.006)| |(-2.046, 7.314)| | |
|λˆhml|-4.582*|ˆhml|-5.903**|ˆhml| |
|ν|-3.203***| |-4.525***| | |
| |(-10.723, 1.560)| |(-12.045, 0.238)| | |
|λˆmom|8.986**|ˆmom| | | |
|ν|-0.412| | | | |
| |(-1.463, 19.436)| | | | |
|λˆg|-9.860***|ˆg|-7.545***|ˆg|-7.282***|
|ν|-4.076***| |-1.781**| |-1.498**|
| |(-17.017, -2.702)| |(-14.722, -0.407)| |(-14.440, -0.125)|
| | | | | |(-3.360, 0.364)|

# 6 Robustness checks

In this section we provide a battery of robustness checks that are summarized in the table below. The exercises are combinations of the following three dimensions: (i) the definition of the greenness and transparency indicator; (ii) the reference sample of individual stocks; and (iii) the definition of the greenness and transparency factor.

Electronic copy available at: https://ssrn.com/abstract=3452649

| |Functional form|γ|Size sample|Factor|
|---|---|---|---|---|
|Rob. 1.1|Eq. (1)|0, 0.2, 0.5, 0.8, 1|946|fg,t|
|Rob. 1.2|Eq. (1)|0, 0.2, 0.5, 0.8, 1|946|f1 g,t|
|Rob. 1.3|Eq. (1)|0, 0.2, 0.5, 0.8, 1|946|f2 g,t|
|Rob. 2.1|Eq. (1)|0, 0.2, 0.5, 0.8, 1|2,154|fg,t|
|Rob. 2.2|Eq. (1)|0, 0.2, 0.5, 0.8, 1|2,154|f1 g,t|
|Rob. 2.3|Eq. (1)|0, 0.2, 0.5, 0.8, 1|2,154|f2 g,t|
|Rob. 3.1|Eq. (9)|n.a.|946|fg,t|
|Rob. 3.2|Eq. (9)|n.a.|946|f1 g,t|
|Rob. 3.3|Eq. (9)|n.a.|946|f2 g,t|
|Rob. 4.1|Eq. (9)|n.a.|2,154|fg,t|
|Rob. 4.2|Eq. (9)|n.a.|2,154|f1 g,t|
|Rob. 4.3|Eq. (9)|n.a.|2,154|f2 g,t|

The first set of exercises (Rob. 1.1 - Rob 2.3) relate to the greenness and transparency indicator as defined in
Equation (1). Rob. 1.1 with γ = 0.5 corresponds to the benchmark specification used in Section 5.2, where we assign
equal weight to the two components of the greenness and transparency indicator, namely the emission intensity and
the environmental transparency of a firm. By tuning the parameter γ, we investigate whether attaching more or less
weight to one of the components of the indicator has an impact on the results. In particular, by imposing γ > 0.5,
we construct an indicator where the quality of a firm’s environmental disclosures has a lower weight compared
to its emission intensity. This version of the indicator attaches a larger weight to hard data and quantitative
information, and a smaller weight to a transparency score which may also rely on descriptive statements and high
level disclosures. Conversely, γ < 0.5 attaches a higher weight to quantitative information and a lower weight to
the overall quality and completeness of environmental disclosures. We also investigate the extreme cases for which
γ = 0 and γ = 1, i.e., the cases for which the indicator Gi,y collapses to the E score Ei,y and to the inverse of the
ranking of emission intensity Ki,y, respectively.

The second set of exercises (Rob. 3.1 - Rob. 4.3) involves a different specification for the greenness and
transparency indicator. In particular, we propose an alternative functional form, where the two components of the
indicator are related to each other in the form of a ratio. In this specification, we use the emission intensity and
the E score as such, while the benchmark specification involves the rankings based on these two indicators. The
alternative definition is thus as follows:

E∗ (Sales)

Gi,y = Ki,y∗ i,y = Ei,y∗

(Emissions)

17

Electronic copy available at: https://ssrn.com/abstract=3452649

where Ei,y is the E score and Ki,y is the ratio of total GHG or CO2 emissions over sales. Unlike the indicator in Equation (1), the indicator based on Equation (9) suffers from a non-linearity issue. In particular, a variation in the denominator corresponds to a more than proportional change in the greenness and transparency indicator. This nonlinearity yields an unstable pattern for the greenness and transparency indicator over time for some companies.

In a further set of robustness checks (Rob.2.1-2.3 and Rob. 4.1-4.3), we expand our sample to include all listed European companies which do some environmental disclosure, i.e. have an E score larger than zero, and those that do no disclosure and belong to brown sectors, as defined in Section 3. By doing so, we more than double the size of the sample, bringing it to 2,154 stocks. However, as discussed in Section 5, enlarging the sample to include mid and small caps may affect the quality of the environmental information used to construct the greenness and transparency indicator. For this reason, in this exercise we still use the greenness and transparency factor as constructed on the smaller, more reliable sample. In particular, the greener and more transparent portfolio and the brown portfolio include the same firms as described in Section 3, hence the factor is the same as in the benchmark exercise described in Section 5. However, this factor is used in Rob.2.1-2.3 and Rob. 4.1-4.3 to price a larger set of assets. Formally, referring to Equation (2), this set of robustness checks involves the same factors ft,k as in the benchmark case, but a larger number of stocks N &gt; n.

Additionally, we check the robustness of the results with respect to the definition of the greenness and transparency factor. In the benchmark case (see Section 5.2) as well as in Rob. 1.1, 2.1, 3.1 and 4.1, we build a portfolio of brown firms selecting the ones belonging to the highest emitting NACE economic sectors, among those that do no environmental disclosure. However, one could argue that the NACE classification is in some cases unsuitable for sustainability analysis. Hence, we build an alternative greenness and transparency factor fg,t based on the returns on the greener and more transparent portfolio ˜g, on the one hand, and those of the portfolio including all non-transparent firms ˜c, on the other. Formally,

fg,t = ˜g − ˜.1 rt rct (10)

Rob 1.2, 2.2, 3.2, and 4.2 perform the estimation of risk premia using the greenness and transparency factor fg,t.

Finally, we test yet another specification for the greenness and transparency factor, only based on transparent firms. In particular, we construct the greenness and transparency factor fg,t as the difference between the returns on the greener and more transparent firms and the firms that do some environmental disclosure, but only attain lower levels of greenness and transparency. The former set of firms correspond to the greener and more transparent portfolio as defined in Section 5, i.e. the one including firms in the top quintile of the distribution of the greenness and transparency indicator. The latter set of firms correspond to those in the lower quintile of the distribution of the greenness and transparency indicator. Formally, the greenness and transparency factor is constructed as

18

Electronic copy available at: https://ssrn.com/abstract=3452649

Also in this case, we test both specifications of the greenness and transparency indicator on the two samples (see Rob. 1.3, 2.3, 3.3 and 4.3).

# Table 5

Table 5 reports the estimated Greenium ˆg and the estimated coefficient ˆg for Rob. 1.1 - Rob. 2.3. The results are based on a four-factor model including the factors in the Carhart model and the greenness and transparency factor.

Focussing on the Greenium, tuning the parameter γ in the benchmark case (i.e., Rob. 1.1) provides results in line with the evidence presented in the previous section. The Greenium is always negative and significant at the 1% confidence level for γ = 0.2, 0.5 and γ = 0.8. Rob. 1.2 and 1.3 use the alternative definitions of the greenness and transparency factor. Building the factor by considering all nontransparent firms instead of only brown firms (Rob. 1.2) still yields a negative and significant Greenium at the 1% level for γ = 0.5 and γ = 0.8, while it is negative and significant at the 5% level for γ = 0.2. Building the factor by considering only transparent firms (Rob. 1.3) yields a negative and significant Greenium for γ = 0.5 and γ = 0.8, at the 5% and 1% confidence level, respectively. Notice that the variation in the size of the Greenium in Rob. 1.2 and 1.3 compared to Rob. 1.1 is purely mechanical, due to the smaller expected value of f g,t and f g,t compared to E[fg,t].

Looking at the lower part of Table 5, Rob. 2.1 - 2.3 estimate the model on the larger sample of European stocks. Considering the benchmark definition for the factor and with γ = 0.5, the Greenium remains negative and significant at the 10% level. Considering the two alternative definitions for the factor, the Greenium remains negative and significant at the 5% and 10% level for Rob. 2.2 and Rob. 2.3, respectively. Varying γ on this larger sample yield a negative Greenium in some instances, but results are generally less strong in terms of significance. Notably, the specifications based on γ = 1, i.e. using only on emission data, are associated with a non-significant Greenium on the larger sample as well.

Focussing on the columns corresponding to extreme values for γ, i.e. γ = 0 and γ = 1, allows us to grasp the importance of the two components of the greenness and transparency indicator. The Greenium is not, or only mildly, significantly different from zero in most exercises. This indicates that only the combination of emission intensity and disclosure quality is generally priced by the market. In no case an indicator based on emissions only (γ = 1) is associated with a significant risk premium, suggesting that investors do not look at emissions only. At the same time, with γ = 0, i.e. when only the completeness of environmental disclosures matters, the Greenium is still negative and significant at 5% or 10% in half of the exercises. This finding suggests that investors do pay attention to the overall quality of firms’ environmental disclosures, over and above their actual emissions.

As for ν, which is linked to the existence of market frictions, the estimates ˆg based on Rob. 1.1. are in line with the results for the risk premium and the cross-sectional parameter ν corresponding to the greenness and transparency factor. Estimation results for the other observable factors are available upon request. The results for these factors are in line with the ones for the benchmark case described in Section 5.2.

Electronic copy available at: https://ssrn.com/abstract=3452649

the benchmark case both in terms of sign and significance for γ = 0.2, 0.8, 1 , while ˆg with γ = 0 is not significantly ν different from zero. Looking at the other robustness checks, ˆg remains generally significant. However, estimates ν of ν tend to lose significance more on the larger sample, because the distribution of the factor loadings bˆi for the greenness and transparency factor is characterized by a larger standard deviation on the larger sample, compared to the distribution of the loadings based on the smaller sample.

Finally, Table 6 shows results using the the greenness and transparency indicator defined in Equation (9). The more unstable behavior of this version of the indicator does not affect the results. The Greenium remains negative and highly significant with the benchmark factor fg,t as well as with f g,t and f g,t (Rob 3.1 - 3.3). The Greenium is still negative on the larger sample considering all the three alternatives for the construction of the factor. However, significance is lower in Rob. 4.2 and Rob. 4.3, while the estimate in Rob. 4.1 is not significant.

Overall, the Greenium remains negative and significant across the majority of the several robustness checks. It tends to loses statistical significance mostly in extreme cases, when we only consider one of the two components of the synthetic greenness and transparency indicator.

20

Electronic copy available at: https://ssrn.com/abstract=3452649

**Table 5: The table reports results for robustness checks Rob. 1.1 - Rob 2.3. The estimated annualized Greenium ˆgλ and the estimated ˆg are computed from the CAR + G model. The greenness and transparency factor is computed based the indicator Gi,y, with γ = 0, 0.2, 0.5, 0.8, 1 and is defined using the alternative specifications fg,t, f g,t and f g,t. Results in the upper part of the table are based on the benchmark sample comprising 946 European individual stocks, while results in the lower part of the table are based on a larger sample comprising 2,154 stocks. ***, ** and * denote significance at 1%, 5% and 10% levels, respectively.**
| |γ = 0|γ = 0.2|γ = 0.5|γ = 0.8|γ = 1|
|---|---|---|---|---|---|
|Rob. 1.1: greenness and transparency factor fg,t|λˆg -5.461*|λˆg -8.290***|λˆg -9.860***|λˆg -9.853***|λˆg -0.152|
| |νˆg 0.574|νˆg -2.860***|νˆg -4.076***|νˆg -5.554***|νˆg -1.477**|
|Rob. 1.2: greenness and transparency factor f g,t1|λˆg 1.308|λˆg -4.611**|λˆg -6.238***|λˆg -7.199***|λˆg -2.757|
| |νˆg 6.138***|νˆg 4.509***|νˆg 3.235***|νˆg 0.821|νˆg 0.808|
|Rob. 1.3: greenness and transparency factor f g,t2|λˆg -3.222|λˆg -1.888|λˆg -4.746**|λˆg -6.648***|λˆg 2.853|
| |νˆg 1.534**|νˆg -1.759***|νˆg -3.280***|νˆg -6.770***|νˆg 1.828***|
| |n = 2,154|n = 2,154|n = 2,154|n = 2,154|n = 2,154|
|Rob. 2.1: greenness and transparency factor fg,t|λˆg -5.056*|λˆg -3.699|λˆg -5.156*|λˆg -4.260|λˆg 3.159|
| |νˆg 0.979|νˆg 1.731**|νˆg 0.628|νˆg 0.071|νˆg 1.833***|
|Rob. 2.2: greenness and transparency factor f g,t1|λˆg 3.209|λˆg -3.448|λˆg -4.531**|λˆg -5.127**|λˆg -3.023|
| |νˆg 8.039***|νˆg 5.671***|νˆg 4.942***|νˆg 2.893***|νˆg 0.542|
|Rob. 2.3: greenness and transparency factor f g,t2|λˆg -5.569**|λˆg -2.781*|λˆg -3.434*|λˆg -4.364**|λˆg 0.990|
| |νˆg -0.813|νˆg -2.652***|νˆg -1.968***|νˆg -4.486***|νˆg -0.035|

**Table 6: The table reports results for robustness checks Rob. 3.1 - Rob 4.3. The estimated annualized Greenium ˆgλ and the estimated ˆg ∗ based the indicator Gi,y. The greenness and transparency factor is defined using the alternative specifications fg,t, f g,t and f g,t. Results in the upper part of the table are based on the benchmark sample comprising 946 European individual stocks, while results in the lower part of the table are based on a larger sample comprising 2,154 stocks. *, ** and *** denote significance at 10%, 5%, and 1% levels, respectively.**
|Factor|fg,t|f g,t1|f g,t2|
|---|---|---|---|
|n = 946|n = 946|n = 946|n = 946|
|Rob. 3.1|λˆg -8.873***|λˆg -6.217***|λˆg -5.692***|
| |νˆg -4.313***|νˆg 2.031***|νˆg -5.303***|
|n = 2,154|n = 2,154|n = 2,154|n = 2,154|
|Rob. 4.1|λˆg -4.330|λˆg -5.240**|λˆg -3.992*|
| |νˆg 0.229|νˆg 3.008***|νˆg -3.603***|

Electronic copy available at: https://ssrn.com/abstract=3452649

# 7 Climate stress test on actual holdings

Based on the estimates derived in the previous section, we carry out a climate stress test on actual investors’ equity holdings. We consider the various institutional sectors at the global level, as well as European SIFIs in particular. The aim of a climate stress test is to measure the exposure of investors to climate risk, in a scenario where more stringent sustainability-oriented policies are progressively implemented, with increasing pressure on comparatively more carbon-intensive firms and sectors. In such a scenario, the expected returns on greener stocks increase, as more sustainable firms are able to distribute higher dividends, while the price of brown stocks drops for the same reason. Notably, one of the first areas where policy pressure may increase, and is in fact already increasing in Europe, is that of environmental disclosures. Against this background, firms that have already implemented suitable non-financial accounting procedures and adopted more advanced environmental reporting standards will be better off once the non-financial disclosure regulation becomes more stringent. In other words, the expected return on stocks of more environmentally sustainable and transparent firms conditional to the implementation of sustainability policies increases. Formally, this implies that the return on the greenness and transparency factor in Equation (7), which is positively correlated with returns on greener and more transparent stocks, increases.

We test the resilience of investors to climate risk by borrowing data on equity exposures and the classification of economic sectors into climate-policy-relevant sectors from Battiston et al. (2017). Following the indication provided by the authors as supplementary information in Table 3, we group individual stocks (see Section 5) according to their associated NACE code. In particular, we classify stocks in the following economic sectors: fossil fuels, energy intensive activities, housing, utilities, transport, finance and other. Table 1 in Battiston et al. (2017) provides aggregate holdings into climate-policy-relevant sectors, as of 2015, for the following institutional sectors: Individuals, Governments (GOV), Non-Financial Companies (NFCs), Other Credit Institutions (OCIs), Other Financial Services (OFSs), as well as the institutional financial sectors as defined in the ESA classification, i.e. Banks, Investment Funds (IFs), and Insurance and Pension Funds (IPFs). Battiston et al. (2017) also classify equity holdings of individual financial institutions by climate-policy-relevant sectors, obtaining the share of their portfolio invested into each of these sectors. Based on their data, we focus on European SIFIs, as identified by the Financial Stability Board.

The equity portfolio of an investor j at time t is defined as follows:

rj,t = ∑ωκrκ,t,7

where ωκ corresponds to the equity exposure to the climate-policy-relevant sector κ and rκ,t is the monthly average value weighted portfolio return of sector κ.

For each institutional sector and individual bank j, we compute the marginal expected shortfall (MES) introduced by Acharya et al. (2010). The MES is defined as the expected equity loss conditional on a particular factor.

Electronic copy available at: https://ssrn.com/abstract=3452649

return taking a loss greater than Γ. In this application we estimate the expected equity loss conditional on the greenness and transparency factor return defined in Equation (7) realizing a gain greater than Γ, i.e. a scenario where greener and more transparent stocks outperform brown stocks by more than a particular threshold. Hence, we can write the MES as follows:

M ESj,t = −E[rj,t| − fg,t < −Γ], (13)

= −E[rj,t|fg,t > Γ]. (14)

We compute the MES considering the following three cases, which are defined in terms of portfolio allocation:

- Baseline Case: the investors’ portfolio allocation is defined as in Equation (12) and reflects the actual allocation of institutional sectors and financial institutions as in Battiston et al. (2017). The portfolio share invested in each of the stocks included in on our sample is derived accordingly.
- Case 1: the investors’ portfolio allocation is defined as rj,t = ∑ωj,1r1,t + ωj,1rt + ∑ωj,κrκ,t, where the exposure to the fossil fuel sector, characterized by the highest emissions, is reduced by 50% compared to the baseline. At the same time, we assume that investments are reallocated to greener and more transparent stocks, defined as the stocks with a positive exposition to the greenness and transparency factor.
- Case 2: the investors’ portfolio allocation is defined as rj,t = ∑ωj,κrκ,t, i.e. only greener and more transparent stocks, as defined above, are included in the portfolio.

In all three cases, the M ESj,t is computed w.r.t. the event fg,t > q0.95, where q0.95 indicates the 95th percentile of the distribution of the greenness and transparency factor. This corresponds to an extreme, but still plausible scenario.

Tables 7 and 8 report MES results for the institutional sectors at the global level and for European SIFIs, respectively. The MES is expressed both as percentage loss and in billions of US dollars. Looking at Table 7, the average MES at the global level in the baseline scenario, i.e. given the actual portfolio allocation in 2015, is estimated to be -1.5%. The very limited variation across institutional sectors and institutions indicates that no one would be immune. A loss of -1.5% on equity portfolios globally corresponds to USD 387 bn. For comparison, this figure is close to the total disbursements under the Troubled Asset Relief Program (TARP), through which the US Government purchased or insured troubled assets between 2008 and 2014. Table 7 also shows what would happen should a global portfolio reallocation take place. The figures obtained under Scenario 1 indicate that halving the exposure to carbon-intensive activities would reduce the MES only marginally. Losses would be avoided only under Scenario 2, characterized by a radical portfolio reallocation.

Turning to Table 8, we estimate a loss of -1.6%, with individual banks recording losses of up to -2.2% on their

23

Electronic copy available at: https://ssrn.com/abstract=3452649

equity portfolio. An average loss of -1.6% for European SIFIs corresponds to almost USD 7 bn. These figures are admittedly not breathtaking, and one might argue that losses of this magnitude would be unlike to trigger a financial crisis. However, this exercise only focuses on equity exposures, and only on first-round losses. Actually, one should consider that a scenario where greener assets very much outperform brown ones would be rooted into a deep transformation of the economy as a whole. The low-carbon transition, if implemented in a sudden and disorderly manner, would be associated with stranded assets and non-performing loans, on top of losses on the stock market, which would also very much weigh on bank’s profits. In fact, only a comparatively small fraction of the overall exposure of banks to carbon-intensive economic sectors is due to banks’ equity holdings. Moreover, the stress-testing literature has shown that second-round effects, such as contagion dynamics, the devaluation of counterparties’ debt obligations, as well as the price impact of fire sales, may considerably amplify first-round losses. In particular, works based on network models show that second-round losses are comparable in magnitude to first round losses (see Battiston et al. (2017) and references therein). Having said that, our data is not granular enough to estimate the amount of second-round losses that could add up to first-round impacts in a scenario like the one we are considering. Moreover, the MES-based stress-testing tool we propose is specifically targeted to assess climate risk in the equity portfolio. However, it’s worth recalling that the global financial crisis, culminating in trillions of losses in world GDP, was triggered by writedowns on the value of loans and securitized assets due to the US subprime crisis, which for many banks amounted to just few billions.

# Table 7

The table reports the M ES in percentage terms and in billions of dollars, for the three scenarios, for global institutional sectors. The M ES is computed conditional to the event fg,t > q0.95.

| | |MES (%)| | |MES (Bn $)| |
|---|---|---|---|---|---|---|
| |Baseline|Scenario 1|Scenario 2|Baseline|Scenario 1|Scenario 2|
|OCIs|-1.592|-1.511|0.113|-8.236|-7.821|0.584|
|Governments|-1.411|-1.259|-0.085|-8.169|-7.286|-0.493|
|Individuals|-1.433|-1.383|0.245|-37.270|-35.964|6.375|
|Banks|-1.495|-1.411|0.062|-40.864|-38.553|1.686|
|IPFs|-1.434|-1.339|0.096|-46.529|-43.460|3.119|
|OFSs|-1.447|-1.376|0.200|-50.261|-47.791|6.931|
|Non-Financial Companies|-1.462|-1.355|0.095|-68.476|-63.444|4.469|
|Investment Funds|-1.404|-1.323|0.211|-127.646|-120.310|19.194|
|Average and Total|-1.460|-1.370|0.117|-387.451|-364.630|41.866|

24

Electronic copy available at: https://ssrn.com/abstract=3452649

**Table 8: The table reports the MES in percentage terms and in billions of dollars, for the three scenarios, for European SIFIs. The MES is computed conditional to the event fg,t > q0.95.**
| |MES (%)| | |MES (Bn $)| | |
|---|---|---|---|---|---|---|
| |Baseline|Scenario 1|Scenario 2|Baseline|Scenario 1|Scenario 2|
|DEUTSCHE BANK AG via its funds|-1.455|-1.321|-0.032|-2.348|-2.131|-0.052|
|BPCE SA via its funds|-1.590|-1.539|0.112|-2.325|-2.251|0.164|
|BNP PARIBAS via its funds|-1.621|-1.518|-0.141|-1.090|-1.021|-0.095|
|UNICREDIT SPA via its funds|-1.482|-1.415|0.145|-0.438|-0.418|0.043|
|BARCLAYS PLC via its funds|-1.512|-1.394|-0.079|-0.572|-0.528|-0.030|
|CREDIT SUISSE GROUP AG via its funds|-1.420|-1.325|0.158|-1.300|-1.212|0.145|
|BANCO SANTANDER SA|-1.912|-1.904|-0.486|-0.155|-0.154|-0.039|
|UBS GROUP AG via its funds|-1.432|-1.314|0.097|-2.604|-2.390|0.176|
|ING BANK NV|-2.225|-2.049|-1.120|-0.042|-0.039|-0.021|
|SOCIETE GENERALE GESTION|-1.571|-1.496|0.088|-0.771|-0.734|0.043|
|Average and Total|-1.647|-1.552|-0.167|-6.971|-6.496|0.222|

# 8 Conclusions and further research

Based on European stocks, we provide evidence of the existence of a pricing factor linked to climate risk and find that the Greenium, i.e. the associated risk premium, is negative and highly statistically significant. This is a novel result in the asset pricing literature. We obtain this result because we take greenness and environmental transparency seriously, unlike studies based on publicly traded funds or indices, which often market themselves as greener than they actually are. To attenuate the problem of greenwashing, we construct an index of greenness and environmental transparency at the individual company level, which takes into account both the GHG emission intensity of a company and the quality of its environmental disclosure. Based on this index we identify the greener and more transparent companies, while we select brown companies among those that do no disclosure, and operate in brown sectors. These two portfolios are used to define the greenness and transparency factor. The negative sign attached to the Greenium indicates that investors buy stacks of greener and more transparent firms accepting a ceteris paribus lower return, as a hedging strategy to reduce their exposure to climate risk. Based on a battery of robustness checks, we show that investors take into account both firms’ GHG emissions and the quality of their environmental disclosures.

In the last part of the paper we use our model to price investors’ equity holdings. We find that their current portfolio allocation exposes them to non-negligible losses in a severe but plausible scenario, where greener and more transparent firms outperform brown firms. We estimate that direct losses could amount to 1.5% of the global equity exposure, and to USD 7 bn for European SIFIs overall. By adding up second-round effects and losses on loans and other assets, this figure could rapidly increase. We calculate that halving investors’ exposure to carbon-intensive activities would decrease losses only marginally, while only a radical portfolio reallocation towards greener assets would ensure resilience. Based on our results, and considering that we only focus on equity exposures, we argue in favor of introducing climate stress tests for systemic financial institutions to make sure that climate risk is suitably addressed.

Electronic copy available at: https://ssrn.com/abstract=3452649

priced. The approach we propose to assess climate risk in equity portfolios is based on a simple and well-known methodology, the marginal expected shortfall, and could easily become part of a broader stress-testing exercise.

Given that the awareness of investors towards climate-related issues has clearly increased in recent years, it would make sense to estimate a model with a time-varying risk premium. As discussed, this presents challenges in terms of estimation, and will be the object of future research. Another interesting avenue relates to the drivers of the Greenium, and in particular to the hypothesis that its negative sign could be driven by an increasing ‘taste for green’ among investors.

26

Electronic copy available at: https://ssrn.com/abstract=3452649

# References

Acharya, V., Pederson, L., Philippon, T., and Richardson, M. (2010). Measuring systemic risk. Technical report, Department of Finance, NYU.

Ahern, K. R. (2013). Network centrality and the cross section of stock returns. USC Marshall Working Paper.

Alok, S., Kumar, N., and Wermers, R. (2020). Do fund managers misestimate climatic disaster risk. The Review of Financial Studies, 33(3):1146–1183.

Ambec, S. and Lanoie, P. (2008). Does it pay to be green? A systematic overview. Academy of Management Perspectives, 22:45–62.

Andersson, M., Bolton, P., and Samama, F. (2016). Hedging climate risk. Financial Analysts Journal, 72(3):13–32.

Ang, A., Hodrick, R., Xing, Y., and Zhang, X. (2006). The cross-section of volatility and expected returns. The Journal of Finance, 61:259–299.

Baker, M. and Wurgler, J. (2006). Investor sentiment and the cross-section of stock returns. The Journal of Finance, 4:1645–1680.

Battiston, S., Mandel, A., Monasterolo, I., Schütze, F., and Visentin, G. (2017). A climate stress-test of the financial system. Nature Climate Change, 7(4):283 – 288.

Battiston, S. and Monasterolo, I. (2018). A carbon risk assessment of central banks’ portfolios under 2◦ C aligned climate scenarios. Working Paper.

Berg, F., Kölbel, J., and Rigobon, R. (2019). Aggregate confusion: The divergence of ESG ratings. Working Paper.

Black, A. and McMillan, D. (2006). Asymmetric risk premium in value and growth stocks. International Review of Financial Analysis, 15(3):237–246.

Bolton, P. and Kacperczyk, M. (2019). Do investors care about carbon risk? Working Paper.

Bragdon, J. H. and Marlin, J. (1972). Is pollution profitable? Risk management, 19(4):9–18.

Campiglio, E., Godin, A., and Kemp-Benedict, E. (2017). Networks of stranded assets: A case for a balance sheet approach. AFD Research Papers.

Carhart, M. (1997). On persistence of mutual fund performance. Journal of Finance, 52(1):57–82.

Carney, M. (2015). Breaking the tragedy of the horizon—climate change and financial stability. Speech given at Lloyd’s of London, September, 29.

Electronic copy available at: https://ssrn.com/abstract=3452649

# References

Chaieb, I., Langlois, H., and Scaillet, O. (2018). Time-varying risk premia in large international equity markets. Working paper.

Chamberlain, G. and Rothschild, M. (1983). Arbitrage, factor structure, and mean-variance analysis on large asset markets. Econometrica, 51(5):1281–1304.

Chatterji, A. K., Durand, R., Levine, D. I., and Touboul, S. (2016). Do ratings of firms converge? implications for managers, investors and strategy researchers. Strategic Management Journal, 37(8):1597–1614.

Choi, D., Gao, Z., and Jiang, W. (2020). Attention to global warming. The Review of Financial Studies, 33(3):1112–1145.

Ciciretti, R., Dalo, A., and Dam, L. (2019). The contributions of betas versus characteristics to the ESG premium. Working Paper.

Cremers, M., Petajisto, A., and Zitzewitz, E. (2012). Should benchmark indices have alpha? Revisiting performance evaluation. Critical Finance Review, 2:1–48.

Daniel, K. D., Litterman, R. B., and Wagner, G. (2016). Applying asset pricing theory to calibrate the price of climate risk. Technical report, National Bureau of Economic Research.

Daniel, K. D. and Titman, S. (1997). Evidence on the characteristics of cross sectional variation in stock returns. Journal of Finance, 53:1–33.

Derwall, J., Guenster, N., Bauer, R., and Koedijk, K. (2005). The eco-efficiency premium puzzle. Financial Analysts Journal, 61(2):51–63.

Donadelli, M., Jüppner, M., Riedel, M., and Schlag, C. (2017). Temperature shocks and welfare costs. Journal of Economic Dynamics and Control, 82:331–355.

Engle, R. F., Giglio, S., Kelly, B., Lee, H., and Stroebel, J. (2020). Hedging climate change news. The Review of Financial Studies, 33(3):1184–1216.

Escrig-Olmedo, E., Fernandez-Izquierdo, M., Ferrero-Ferrero, I., Rivera-Lirio, J., and Muñoz-Torres, M. (2019). Rating the raters: Evaluating how ESG rating agencies integrate sustainability principles. Sustainability, 11:915.

Fama, E. F. and French, K. R. (1993). Common risk factors in the returns on stocks and bonds. Journal of Financial Economics, 33(1):3–56.

Fama, E. F. and French, K. R. (2007). Disagreement, tastes, and asset prices. Journal of financial economics, 83(3):667–689.

Fama, E. F. and French, K. R. (2008). Dissecting anomalies. Journal of Finance, 63(4):1653–1678.

Electronic copy available at: https://ssrn.com/abstract=3452649

# References

Fama, E. F. and French, K. R. (2015). A five-factor asset pricing model. Journal of Financial Economics, 116(1):1–22.

Gagliardini, P., Ossola, E., and Scaillet, O. (2016). Time-varying risk premium in large cross-sectional equity datasets. Econometrica, 84(3):985–1046.

Gagliardini, P., Ossola, E., and Scaillet, O. (2019). A diagnostic criterion for approximate factor structure. Journal of Econometrics, 212(2):503–521.

Goergen, M., Jacob, A., Nerlinger, M., Riordan, R., Rohleder, M., and Wilkens, M. (2019). Carbon risk. Technical report, University of Augsburg, Queen’s University.

Gore, A. (1993). Earth in the Balance: Ecology and the Human Spirit. New York: Penguin.

Gros, D., Lane, P., Langfield, S., Matikainen, S., Pagano, M., Schoenmaker, D., and Suarez, J. (2016). Too late, too sudden: Transition to a low-carbon economy and systemic risk. Technical report, European Systemic Risk Board.

Hartzmark, S. M. and Sussman, A. B. (2019). Do investors value sustainability? a natural experiment examining ranking and fund flows. The Journal of Finance, 74(6):2789–2837.

Haugen, R. and Baker, N. (1996). Commonality in the determinants of expected stock returns. Journal of Financial Economics, 41:401–439.

Hoepner, A. G. F., Oikonomou, I., Sautner, Z., Starks, L. T., and Zhou, X. (2018). ESG shareholder engagement and downside risk. AFA 2018 paper.

Hong, H., Li, F. W., and Xu, J. (2019). Climate risks and market efficiency. Journal of Econometrics, 208(1):265–281.

Jagannathan, R. and Wang, Z. (2002). Empirical evaluation of asset-pricing models: a comparison of the sdf and beta methods. Journal of Finance, 57(5):2337–2367.

Lintner, J. (1965). The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets. Review of Economics and Statistics, 47(1):13–37.

Marquis, C., Toffel, M. W., and Zhou, Y. (2016). Scrutiny, norms, and selective disclosure: A global study of greenwashing. Organization Science, 27(2):483–504.

Monasterolo, I. and De Angelis, L. (2020). Blind to carbon risk? an analysis of stock market reaction to the Paris Agreement. Ecological Economics, 170:106571.

Electronic copy available at: https://ssrn.com/abstract=3452649

# References

Monasterolo, I., Zheng, J. I., and Battiston, S. (2018). Climate transition risk and development finance: A carbon risk assessment of china’s overseas energy portfolios. *China & World Economy*, 26(6):116–142.

Oikonomou, I., Brooks, C., and Pavelin, S. (2012). The impact of corporate social performance on financial risk and utility: A longitudinal analysis. *Financial Management*, 41(2):483–515.

Pindyck, R. S. (2013). Climate change policy: what do the models tell us? *Journal of Economic Literature*, 51(3):860–72.

Porter, M. (1991). America’s green strategy. *Scientific American*, 264(4):168.

Porter, M. and van der Linde, C. (1995). Toward a new conception of the environment-competitiveness relationship, *Journal of Economic Perspective*, 9(4), 97–118.

Renneboog, L., ter Horst, J. R., and Zhang, C. (2007). Socially responsible investments: Methodology, risk exposure and performance. TILEC Discussion Paper No. 2007-013.

Seitz, J. (2010). Nachhaltige investments: eine empirisch-vergleichende analyse der performance ethisch-nachhaltiger investmentfonds in europa. Hamburg: Diplomica Verlag.

Sharpe, W. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *Journal of Finance*, 19(3):425–442.

Short, J. L. and Toffel, M. W. (2008). Coerced confessions: Self-policing in the shadow of the regulator. *The Journal of Law, Economics, & Organization*, 24(1):45–71.

Statman, M. (2000). Socially responsible mutual funds (corrected). *Financial Analysts Journal*, 56(3):30–39.

Trinks, A., Scholtens, B., Mulder, M., and Dam, L. (2018). Fossil fuel divestment and portfolio performance. *Ecological Economics*, 146:740–748.

30 Electronic copy available at: https://ssrn.com/abstract=3452649

# Appendix: Additional tables and figures

Figures 2 and 3 show the time-series of the greenness and transparency indicator Gi,y (top panels) for two representative companies, as well as their ranking in terms of E score and emission intensity over time. The bottom panels plot the firms’ E score over time, as well as their emission intensity. NIBE Industrier AB develops solutions for smart heating and intelligent control in industry and infrastructure. International Airlines Group is the largest airline group globally. The greenness and transparency indicator for the two companies differs by three orders of magnitude. For NIBE Industrier AB, the quality and quantity of disclosures have improved over time, together with a slightly decreasing emission intensity, both resulting in an increasing value for the greenness and transparency indicator over time. International Airlines Group attained an E score in 2011 which was comparable to that of NIBE Industrier AB in 2009. However, International Airlines Group’s disclosures only marginally improved over time, if at all. With respect to emissions, they are obviously incomparably larger for airlines than for many other companies.

31

Electronic copy available at: https://ssrn.com/abstract=3452649

# NIBE Industrier AB

| |2009|2010|2011|2012|2013|2014|2015|2016|2017| | |
|---|---|---|---|---|---|---|---|---|---|---|---|
|Score|100|90|80|70|60|50|40|30|20|10|0|
|Emissions Intensity|5|4.5|4|3.5|3|2.5|2|1.5|1|0.5| |

Figure 2: Greenness and transparency indicator GN IBE,y , E score and emissions intensity in ranked and row values, of the NIBE Industrier AB.

Electronic copy available at: https://ssrn.com/abstract=3452649

# International Airlines Group

| |2011|2012|2013|2014|2015|2016|2017|
|---|---|---|---|---|---|---|---|
|Emissions Intensity|0|100|200|300|400|500|600|
|GIntAir,y|0|10|20|30|40|50|60|
|E Score|0|70|80|90|100|110|120|

Figure 3: Greenness and transparency indicator GIntAir,y, E score and emissions intensity in ranked and raw values, of the International Airlines Group.

Electronic copy available at: https://ssrn.com/abstract=3452649

# Table 9: List of highest-emitting economic sectors. Source: Eurostat.

|Description|NACE Rev 2 Code|
|---|---|
|Mining of coal and lignite|B05|
|Extraction of crude petroleum and natural gas|B06|
|Mining of metal ores|B07|
|Mining support service activities|B09|
|Manufacture of coke and refined petroleum products|C19|
|Manufacture of chemicals and chemical products|C20|
|Manufacture of rubber and plastic products|C22|
|Manufacture of other non-metallic mineral products|C23|
|Manufacture of basic metals|C24|
|Manufacture of fabricated metal products, except machinery and equipment|C25|
|Electricity, gas, steam and air conditioning supply|D35|
|Sewerage|E37|
|Waste collection, treatment and disposal activities; materials recovery|E38|
|Remediation activities and other waste management services|E39|
|Land transport and transport via pipelines|H49|
|Water transport|H50|
|Air transport|H51|

# Table 10: List of brown companies in 2017.

|Company Name|NACE code|Company Name|NACE code|
|---|---|---|---|
|Lubelski Wegiel Bogdanka SA|B05|Ibstock PLC|C23|
|Genel Energy Plc|B06|Rhi Magnesita NV|C23|
|Norwegian Energy Co ASA|B06|Bossard Holding AG|C25|
|BHP Billiton PLC|B07|Beijer Alma AB|C25|
|Grupa Kety SA|B07|Indus Holding AG|C25|
|Stalprodukt SA|B07|Boryszew SA|C25|
|Alumetal SA|B07|Mennica Polska SA|C25|
|Elkem ASA|B07|SFS Group AG|C25|
|Northern Drilling Ltd|B09|Fiskars OYJ Abp|C25|
|Bonheur ASA|B09|Elektrobudowa SA|D35|
|Borr Drilling Ltd|B09|Kogeneracja|D35|
|Shelf Drilling Ltd|B09|BKW AG|D35|
|Odfjell Drilling Ltd|B09|Arendals Fossekompani A/S|D35|
|EMS-Chemie Holding AG|C20|Nobina AB|H49|
|Ciech SA|C20|PKP Cargo SA|H49|
|Tikkurila Oyj|C20|Dfds A/S|H50|
|Tessenderlo Group SA|C20|Fjord1 ASA|H50|
|Recticel SA|C22|Ocean Yield ASA|H50|
|Sanok Rubber Co SA|C22|Frontline Ltd/Bermuda|H50|
|Forbo Holding AG|C22|Wizz Air Holdings Plc|H51|
|Vidrala SA|C23| | |

34

Electronic copy available at: https://ssrn.com/abstract=3452649

# Table 11: Estimated annualized risk premia ˆk and the cross-sectional estimator ˆk for the factors in the Carhartλ ν model and the greenness and transparency factor fg,t as in Equation (7). The factor fg,t is built based on the deciles and terciles of the distribution of the greenness and transparency indicator. Confidence intervals are reported at the 99% level. ***, ** and * denote significance at 1%, 5% and 10% levels, respectively.

# Panel A: greener and more transparent portfolio includes top decile firms

|ˆm λ|10.592*|ˆm ν|4.557***|
|---|---|---|---|
| |(-4.982, 26.164)| |(3.805, 5.309)|
|ˆsmb λ|3.306*|νˆsmb|1.635***|
| |(-1.375, 7.986)| |(0.65, 2.62)|
|ˆhml λ|-4.805**|νˆhml|-3.427***|
| |(-10.947, 1.337)| |(-4.745, -2.109)|
|ˆmom λ|9.203**|ˆmom ν|-0.196|
| |(-1.247, 19.653)| |(-2.881, 2.491)|
|λˆg|-10.479***|νˆg|-4.948***|
| |(-17.298, -3.661)| |(-7.187, -2.708)|

# Panel B: greener and more transparent portfolio includes top tercile firms

|ˆm λ|10.669*|ˆm ν|4.634***|
|---|---|---|---|
| |(-4.904, 26.241)| |(3.886, 5.383)|
|ˆsmb λ|3.471*|νˆsmb|1.8***|
| |(-1.21, 8.151)| |(0.828, 2.772)|
|ˆhml λ|-4.635*|νˆhml|-3.257***|
| |(-10.776, 1.507)| |(-4.56, -1.953)|
|ˆmom λ|8.246**|ˆmom ν|-1.152|
| |(-2.204, 18.696)| |(-3.968, 1.664)|
|λˆg|-8.612***|νˆg|-3.331***|
| |(-15.787, -1.437)| |(-5.428, -1.234)|

# Table 12: Companies’ fundamentals (year 2017). The table reports descriptive statistics for size (measured by the log of total assets), leverage and RoA, considering companies included in the various portfolios.

|Portfolio|Size Mean|Size Std|Leverage Mean|Leverage Std|RoA Mean|RoA Std|
|---|---|---|---|---|---|---|
|R˜1|9.683|1.013|25.933|16.168|6.619|5.790|
|R˜2|9.368|1.099|23.027|15.349|6.474|6.825|
|R˜3|9.440|1.258|22.208|16.330|6.685|6.741|
|R˜4|9.496|1.201|22.019|14.405|6.977|7.577|
|R˜g|9.513|1.184|23.466|15.666|5.526|6.585|
|R˜|9.473|1.158|23.196|15.365|6.627|6.922|
|R˜c|9.368|1.201|24.018|16.372|7.187|8.208|
|R˜b|9.433|1.164|24.888|17.461|7.163|8.077|

# Table 13: Descriptive statistics for portfolios including transparent firms. The table reports the mean and standard deviation (Std), kurtosis (Kurt) and skewness (Skew), the Sharpe ratio, t-stat for the null hypothesis that the mean return is zero. Portfolio ˜5 is the top green and transparent.

|Portfolio|Mean|Std|Kurt|Skew|Sharpe|t-stat|
|---|---|---|---|---|---|---|
|R˜1|1.065|0.503|3.579|-0.099|0.212|2.611|
|R˜2|1.160|0.547|5.257|-0.684|0.212|2.617|
|R˜3|0.786|0.530|4.175|-0.391|0.148|1.827|
|R˜4|0.920|0.489|3.445|-0.232|0.188|2.317|
|R˜5|0.943|0.502|4.097|-0.593|0.188|2.315|

Electronic copy available at: https://ssrn.com/abstract=3452649

# Table 14: Estimates of linear factor models on various portfolios including transparent firms, with an increasing degree of greenness and transparency from 1 to 4. Results are reported for the following models: four-factor Carhart model (CAR), three-factor Fama-French model (3FF) and the CAPM. ***, ** and * denote significance at 1%, 5% and 10% levels, respectively.

|Portfolio| |R˜1|R˜2|R˜3|R˜4|
|---|---|---|---|---|---|
|CAR model|ˆa|0.005***|0.007***|0.003***|0.004***|
|ˆm| |0.925***|1.004**|0.991***|0.931***|
|ˆsmb| |-0.119|-0.052|-0.202***|-0.255***|
|ˆhml| |-0.103|-0.289***|-0.317***|-0.205***|
|ˆmom| |0.144***|-0.057|-0.050|0.086***|
| |R2adj|0.878|0.916|0.941|0.938|
|3FF model|ˆa|0.006***|0.006***|0.003***|0.005***|
|ˆm| |0.902***|1.014***|0.999***|0.916***|
|ˆsmb| |-0.131|-0.048|-0.198***|-0.262***|
|ˆhml| |-0.194**|-0.252***|-0.285***|-0.260***|
| |R2adj|0.87|0.915|0.940|0.935|
|CAPM|ˆa|0.006***|0.007***|0.003**|0.005***|
|ˆm| |0.860***|0.958***|0.938***|0.861***|
| |R2adj|0.864|0.908|0.926|0.917|

Electronic copy available at: https://ssrn.com/abstract=3452649