# Accelerating Climate Action with AI

November 2023

By Amane Dannouni, Stefan A. Deutscher, Ghita Dezzaz, Adam Elman, Antonia Gawel, Marsden Hanna, Andrew Hyland, Amjad Kharij, Hamid Maher, David Patterson, Edmond Rhys Jones, Juliet Rothenberg, Hamza Tber, Maud Texier, and Ali Ziat

# Boston Consulting Group

partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

# Contents

# 01

Foreword

# 02

Executive Summary

# 05

The Climate Action Imperative and the Promise of AI

# 09

How AI Can Help Accelerate Climate Action

# 22

Navigating AI’s Potential Risks

# 28

AI for Climate: A Summary of Critical Policy Outcomes

# 41

Endnotes

# 43

About the Authors

# 45

Acknowledgements

# 47

References

# Foreword

This report aims to provide policymakers, corporate decision makers, and climate leaders with a clear and concise understanding of the role that artificial intelligence (AI) can play in climate action.

More specifically, its goals are to highlight AI’s significant potential to help address our environmental challenges, to shed light on climate-relevant AI risks, and to offer policymakers a streamlined framework for desirable policy outcomes.

Throughout the report, we share examples of successful early applications of AI for climate and of instances in which policymakers have already taken the initiative to enable, promote, or guide the use of AI for climate action across sectors. This work draws on interviews with a range of climate change and AI experts, builds on previous research from organizations including Climate Change AI and the AI for the Planet Alliance, and leverages BCG’s analysis and client experience as well as Google’s technical and operational expertise—and its experience in developing solutions.

# 1 ACCELERATING CLIMATE ACTION WITH AI

# Executive Summary

Accelerating climate action is imperative, as we are on a path to fall short of the Paris Agreement’s goal to keep warming under 1.5° Celsius.

- The United Nations Intergovernmental Panel on Climate Change (IPCC) estimates that, based on action to date, the world will likely see warming of 2.8°C with catastrophic consequences.

While AI is only just starting to be applied to climate challenges, leading-edge organizations and use cases are already delivering results—and demonstrating the promise of AI for climate—along three dimensions.

- Information. AI-curated information sources are aiding nations in shaping their climate strategy—and in responding to emergencies such as wildfires.
- The IPCC forecasts that in order to meet the 1.5°C goal, the world will need to reduce emissions—from the baseline of 2010 levels—by 43% by 2030.

By scaling currently proven applications and technology, artificial intelligence (AI) has the potential to unlock insights that could help mitigate 5% to 10% of global greenhouse gas (GHG) emissions by 2030—and significantly bolster climate-related adaptation and resilience initiatives.

- Prediction. AI’s predictive power is helping save lives by offering advance warning of floods.
- Optimization. AI applications are enabling organizations to understand and reduce their Scope 1, 2, and 3 carbon footprints.1

AI also poses risks that must be considered and managed thoughtfully to ensure its use has a net positive impact on climate.

- 87% of executives view AI as having the potential to address climate issues.
- AI’s positive impact will be multiplied should it contribute to scientific breakthroughs that open new pathways for climate action.

AI can contribute to climate action by reducing emissions, guiding adaptations to unavoidable climate change impacts, and providing foundational capabilities that enable climate action.

- Mitigation. Helping with both the reduction and removal of emissions—and with the underlying measurement needed to size the challenge and track progress.
- Adaptation and Resilience. Aiding countries, regions, cities, citizens, and businesses in forecasting climate-related hazards, developing plans to address them, and responding in real time to crises.
- Foundational Capabilities. Enabling climate-related modeling, research into climate economics, and new approaches to climate education and supporting breakthroughs in fundamental research.

Energy-Related GHG Emissions. A 2022 paper in Nature Climate Change estimates that cloud and hyperscale data centers are responsible for 0.1%–0.2% of global GHG emissions and that roughly 25% of data center workloads are related to machine learning (ML). Yet, newer and more complex AI models may require more energy. At present, robust forecasts for AI’s future energy requirements remain elusive given uncertain adoption rates and the broad spectrum of potential technical advancements with the potential to decrease AI’s energy intensity. Nonetheless, AI providers are already striving to enhance energy efficiency and integrate clean energy sources.

Water Use. Water-based cooling remains the most energy-efficient option for data centers, and its overall impact on water consumption is low. In 2016 in the US, data centers were estimated to have used less than 0.02% of the country’s water consumption for cooling. Nevertheless, in some cases, water-based cooling can put pressure on local water resources. Data center operators have begun to address this issue by providing more disclosure, exploring new cooling techniques, and investing in replenishment initiatives.

BOSTON CONSULTING GROUP GOOGLE

•  Waste. While data centers currently account for only a small fraction of the world’s e-waste challenge, there is an opportunity for tech firms to build on early circularity successes and take a more thoughtful approach embracing more recycling and reuse.

•  Other Potential Risks. AI applications should be sustainable and equitable by intention. AI can be applied to both climate-friendly and climate-unfriendly applications, can narrow or widen disparities between the Global North and the Global South, and can be trained on data sets that reflect the world’s diversity. Leaders and model builders need to be mindful in their design choices.

Policymakers have a critical oversight role to play in maximizing the benefits from AI-driven climate action while minimizing its risks. Critical policy outcomes to pursue include the following:

- Enabling AI for climate progress by encouraging data sharing, ensuring affordable technology access, building awareness, and investing in talent
- Accelerating the deployment of AI for climate by defining public and private sector priorities, delivering on public sector use cases, and encouraging private sector action
- Promoting environmentally and socially responsible deployment of AI

# 3 ACCELERATING CLIMATE ACTION WITH AI

# How We Define Artificial Intelligence

According to the Massachusetts Institute of Technology, AI is defined as the ability of computers to imitate human cognitive functions such as learning and problem-solving, using math and logic to simulate the process of reasoning that helps humans learn from new information and make decisions.

For the purposes of this report, we are using a broader definition of AI that comprises a set of mathematical and computer science techniques aimed at analyzing data to help understand and navigate real-world phenomena through:

- providing better information (descriptive use cases),
- delivering improved predictions (predictive use cases), and
- suggesting optimization moves and recommendations to reach targets (prescriptive use cases).

These goals can be attained by applying a wide range of techniques including those in the table below—all of which we include in this report’s definition of AI.

Applying AI to real-world problems is common practice today. The technology has proven its ability to help public and private organizations have a better understanding of their context, provide better services, and improve their operational performance.

|Technology|General Example|Climate-Related Example|
|---|---|---|
|Advanced Analytics|Supermarket Inventory Management. Advanced analytics can identify best sellers and demand dynamics, enabling more efficient shelving and restocking strategies, thereby reducing waste and ensuring popular items are always in stock.|Energy Consumption Optimization. Advanced analytics can optimize a building’s carbon footprint by adjusting heating, cooling, and lighting systems in response to real-time data from sensors and weather forecasts.|
|Machine Learning|Credit Card Fraud Detection. Machine learning helps banks and credit card companies detect unusual transactions, enabling them to alert card holders and minimize fraud losses.|Predicting Wildfires. Machine learning models can analyze weather data, satellite imagery, and terrain information to predict the likelihood of wildfires, helping authorities take preventive measures and optimize resource allocation.|
|Deep Learning|Medical Image Evaluation. Applied to the analysis of medical images such as X-rays and MRIs, deep learning helps doctors diagnose diseases and other abnormalities more accurately, enabling more timely and effective treatments.|Extreme Weather Prediction. Deep learning can analyze vast amounts of historical and real-time meteorological and satellite data, leading to more accurate forecasts for hurricanes, tornadoes, and typhoons.|
|Large Language Models|Customer Service Chatbots. Large language models enable companies to automate the process of answering customer questions and helping troubleshoot issues, enhancing the efficiency of, and satisfaction with, customer service operations.|Green Technology Innovation. Large language models can accelerate innovation by digesting research papers and patent applications and rapidly surfacing ideas and identifying knowledge gaps.|

BOSTON CONSULTING GROUP GOOGLE

# The Climate Action Imperative and the Promise of AI

Despite significant progress over the last several years in mobilizing the global community to intensify its climate actions and ambitions, the world is not on track to meet the Paris Agreement’s target to limit temperature rise to 1.5°C. This target was selected because scientists believe that above that level, the effects would be catastrophic and potentially irreversible. At present—based on updated national pledges since COP26 in 2021—the United Nations Environment Programme currently estimates that we are on a path to warming by 2.8°C.

Even if the world succeeds in limiting warming to 1.5°C, there will still be adverse impacts. Already today at 1.1°C, the IPCC reports that over 3 billion people live in areas highly vulnerable to climate impacts. We are already seeing the impact on weather, agriculture, water security, and migration. If we overshoot the target, the picture becomes increasingly dire: seas will rise further, droughts will be worse, and extreme weather events will be more common.

# ACCELERATING CLIMATE ACTION WITH AI

In a 1.5°C world, the IPCC forecasts that 48% of the world’s population will be exposed to deadly heat levels for more than 20 days a year. In a 3° to 4°C world, that number increases to 74%. If we stay on our current trajectory, the World Bank estimates an additional 143 million people—more than the combined populations of the United Kingdom, Morocco, and Malaysia—could be displaced. And, absent significant investments in resilience, major global cities—for example, Tokyo, Osaka, Mumbai, Bangkok, New York, London, and Lagos—will find themselves partly under water.

We urgently need new tools to accelerate the reduction and removal of GHG emissions—and to help citizens, cities, regions, countries, and businesses make plans to adapt to the inevitable impacts of warming. AI offers much promise.

# Climate Action Has an Analytical Challenge— and AI Can Help

Leaders increasingly understand the urgency. So far, 194 parties to the Paris Agreement have developed Nationally Determined Contributions (NDCs)—each representing detailed commitments for how their country will help the world meet the Paris Agreement’s 1.5°C goal—up from 75 parties in February 2021.

But avoiding the most catastrophic impacts of warming requires more than political will. To achieve real progress, we need to develop a much richer analytical understanding of a complex system comprising many variables and feedback loops. (See Exhibit 1.)

# Exhibit 1 - Climate is an interlinked, multi-parameter system

| | |Core climate characteristics| |
|---|---|---|---|
|Human activities, such as fossil fuel burning and land use changes, create significant volumes of greenhouse gas.| | | |
|Increase in impermeable surfaces|Urbanization| | |
| |Water|Emissions have varying impacts on core climate characteristics, and changes in these processes can worsen the greenhouse gas effect.| |
|Changes in precipitation|Temperature| | |
|Salinity|Ice cap melting| | |
|Ocean circulation upheaval|Clouds| | |
|Carbon cycle disturbance|Average temperature rise| | |
|Global warming|Gulf Stream modification| | |
|Abrupt climate change|Europe cooling| | |
|Land use changes|Sea level rise| | |
|CO2|NO2| | |
|CH4|Fluctuations in climate characteristics drive major impacts—natural, physical, and socioeconomic—at both local and global scales.| | |
| | |Cyclones|Food|
|Heat waves| |Droughts| |
|Disease spread|Disasters| | |
|Biodiversity losses|Casualties| | |
|Economic losses|Famines| | |
| | |Major impacts| |

Source: Philippe Rekacewicz, Emmanuelle Bournay, UNEP/GRID-Arendal; BCG analysis.

BOSTON CONSULTING GROUP GOOGLE

Developing models is essential to understanding the relationships among variables—and to anticipating the likely impact of different strategies and choices. But modeling these complex interconnections on a local and global scale is a huge challenge. It requires assembling massive, longitudinal, and real-time global data sets. Information is needed on climate (for example, temperatures, ocean processes, and meteorological phenomena) and on human activities (for example, emissions, and land use changes). And not all the necessary data is even available.

But understanding the complex systems that drive climate-relevant outcomes is exactly the kind of challenge at which AI excels. By amalgamating and processing massive data sets, AI can reveal elusive patterns and valuable insights, facilitate scenario development and prediction, accelerate the evaluation of multiple courses of action, enable operational optimizations, and help monitor progress toward predefined goals.

# Estimating AI’s Potential Contribution

Based on our research and experience, the three broad areas in which AI can accelerate climate progress are the following:

- Mitigation. Helping with both the reduction and removal of emissions—and with the underlying measurement needed to size the challenge and track progress
- Adaptation and Resilience. Aiding citizens, countries, regions, cities, and businesses to prepare for and respond to the inevitable impacts of a warming planet
- Foundational Capabilities. Enabling climate action via improvements in climate modeling, climate economics, and climate education, as well as accelerating breakthrough innovations that will open new horizons for climate action

Business leaders agree. In a 2022 BCG survey of senior executives with leadership roles related to climate or AI (see AI is Essential for Solving the Climate Crisis), 87% viewed AI as a helpful unlock for climate issues. They saw supporting emissions reduction as the top climate use case for AI in their organizations, but expressed interest in other applications as well. (See Exhibit 2.)

# Exhibit 2 - Leaders believe AI can play a role in climate action, especially in helping to reduce emissions

|In which areas of climate-related advanced analytics and AI do you see the greatest business value for your organization? (%)|In which areas of climate-related advanced analytics and AI do you see the greatest business value for your organization? (%)|
|---|
|Reducing emissions|61%|
|Measuring emissions|57%|
|Predicting hazards|44%|
|Managing vulnerabilities|42%|
|Removing emissions|37%|
|Facilitating climate research, climate economics, and education|28%|

Source: BCG Climate AI survey 2022. All respondents have decision-making authority over climate or AI topics at their organizations. Respondents were permitted to give more than one answer.

7 ACCELERATING CLIMATE ACTION WITH AI

# Emissions Reduction Potential

Regarding emissions reduction potential, a 2021 BCG study (see Reduce Carbon and Costs with the Power of AI) estimates that currently proven AI-enabled use cases could reduce emissions by 5% to 10% by 2030. If that potential is fully realized, AI-driven applications would be responsible for achieving roughly between 10% and 20% of the IPCC’s 2030 interim emissions-reduction target for the world to achieve net zero by 2050.5 Similarly, a Microsoft/PwC study looking at four sectors (agriculture, energy, transport, and water) estimates that AI has the potential to reduce global GHG emissions by 4%.6 Further, respondents in a Capgemini survey of companies that had leveraged AI for climate action reported that their efforts to date had achieved GHG reductions of between 11.3% and 14.3% depending on the sector—and these executives believe that AI could reduce overall GHG emissions by 15.9% in the next three to five years.7

# Adaptation and Resilience

On adaptation and resilience, AI can help cities forecast their climate vulnerability, develop estimates of the cost of inaction, and model the impact of different climate interventions. These insights can aid them in identifying the actions with the greatest benefit, generating private-sector enthusiasm for funding investable projects, and securing public and philanthropic support for essential, but non-bankable, adaptations. It also can help guide real-time decision-making in agriculture—for example, increasing crop production through intelligent irrigation systems—or in fast-moving crises such as wildfires.

# Foundational Capabilities

And AI offers many foundational capabilities that support both short-term and long-term climate action. For example, it can support today’s climate research with higher-fidelity climate change simulations. But it also has the potential to accelerate breakthrough innovations in domains such as physics, chemistry, biology, and material science that could “bend the curve” on climate progress.

All of our estimates are based on the current state of AI technology—and thus speak primarily to AI’s potential in currently proven applications. Today, we are in the early stages of the adoption curve. Transforming potential to achievement will require that all organizations fully embrace AI as an essential enabler of their climate actions. And it is important to note that our assessment does not encompass major AI-driven disruptions and breakthroughs—for example, new materials for batteries, new drought-resistant crops, novel carbon removal technologies, and scalable approaches to nuclear fusion—that could unlock massive positive impact.

# The Promise of AI

The promise of AI is real. While we are already seeing benefits, we need to accelerate its contribution to planet-saving climate impact. The next chapter offers a deeper dive into the primary known climate-related use cases for AI—and highlights some examples of how and where AI is already making a positive difference.

BOSTON CONSULTING GROUP GOOGLE

# How AI Can Help Accelerate Climate Action

It has demonstrated the potential to enable and catalyze climate progress in three broad areas: taking emissions mitigation to the next level, shaping strategies for adaptation and resilience, and supporting both climate research and reinforcing technologies. Some AI applications are in early stages, some are being tested, and others are already being scaled. But all will need to be embraced more broadly if we are to fulfill the promise of AI to limit warming to less than 1.5°C.

Exhibit 3 summarizes the most promising of the currently known AI use cases for climate. The rest of this chapter will offer more detail on each, along the way highlighting inspiring examples of how AI is helping unlock and accelerate climate progress.

# AI’s Role in Emissions Mitigation

Getting smarter on reducing and removing emissions is essential. And AI is already delivering significant wins that need to be scaled. Its contributions fall into two broad areas: measurement and monitoring, and reduction and removal.

# Measurement and Monitoring

Without reliable, clean, and independently verifiable data, effective climate action is difficult. Countries and companies need to know their baselines and track their progress, both at the macro level (“What are our total GHG emissions?”) and the micro level (“Which aspects of our operations and broader supply chain are the big drivers? Are our efforts at reduction or removal delivering the expected results?”).

# Exhibit 3 - Key AI applications to accelerate climate progress

|Mitigation|Adaptation and Resilience|
|---|---|
|Measurement & Monitoring|Hazard Prediction|
|Macro-level measurement|Building early warning systems|
|e.g., calculating carbon footprint at the country level|e.g., predicting near-term extreme events such as flooding, drought, and cyclones|
|Micro-level measurement|Vulnerability Management|
|e.g., calculating carbon footprints of individual products|e.g., monitoring drought and wildfire spread|
|Supporting nature-based & technological removal|Building resilient infrastructure & protecting biodiversity|
|e.g., assessing natural carbon stocks|e.g., intelligent irrigation, monitoring of endangered species|

# Foundational Capabilities

- Climate modeling e.g., monitoring drought and wildfire spread
- Climate economics e.g., developing cost of inaction assessments
- Education & behavioral change e.g., developing recommendations for climate-friendly consumption
- Innovation & breakthroughs e.g., supporting research on fusion

Effective measurement and monitoring solutions leverage AI to process and analyze data from multiple sources such as satellite data, weather data, sensors, and other heavy data sets—which can, for example, help an organization develop a baseline for its Scope 1, 2, and 3 emissions. AI can also deliver insights, revealing patterns in emissions and suggesting the best ways to prioritize abatement efforts.

In the domain of macro-level measurement, Climate TRACE has been an early mover. This nonprofit offers free emissions data for more than 80,000 individual sources and facilities around the globe, providing a data foundation to help organizations get started with mitigation plans. Its data could, for example, assist countries seeking to transition away from coal and other fossil-fuel based electricity generation by pinpointing the largest emitters and revealing the mix of power sources by region. (See the sidebar Climate TRACE: Providing Timely, Independent Emissions Data—for Free.)

Solutions are emerging for micro-level measurement as well. Google’s Environmental Insights Explorer (EIE) uses machine learning to offer city planners annual estimates of emissions from buildings and transportation, tree canopy status, and emissions reduction opportunities such as the potential for expanded rooftop solar. Houston, Texas, used EIE to perform a solar assessment and inform the development of its 5 million MWh Solar Energy Target Plan. Similarly, CO2 AI, a novel SaaS platform, enables business leaders—together with their value chain partners—to develop an accurate estimate of their organizations’ Scope 1, 2, and 3 emissions down to the product level. It also helps them to model and evaluate emissions reduction opportunities. (See the sidebar CO2 AI: Helping Business Ecosystems Reduce their Carbon Footprints.)

Source: BCG, AI for the Planet Alliance.

# Climate TRACE: Providing Timely, Independent Emissions Data—for Free

Making real progress on climate requires timely and accurate data on emissions to inform government policy and business action. But historically, emissions data has been based on self-reporting, calculated using varying algorithms, and submitted years after the fact. Climate TRACE—a global coalition of nonprofits, tech startups, and researchers—offers a powerful, free, and independent alternative: the first comprehensive source-level global inventory of GHG emissions.

Supported by Google.org, among others, Climate TRACE uses AI and machine learning to calculate GHG emissions on a global scale, with the goal of moving toward real-time precision. To achieve this, its model analyzes more than 59 terabytes of data from over 300 satellites and more than 11,000 sensors to create highly granular emissions data for over 80,000 sources globally. That number is expected to grow to more than 70 million sources by the end of 2023.

# Application area: Macro-Level Measurement

|Climate TRACE tracks global emissions|EURD|56.15|B TONNES of CO2 in 2021|
|---|---|---|---|
|Source: Climate TRACE. Used with permission.|Source: Climate TRACE. Used with permission.|Source: Climate TRACE. Used with permission.|Source: Climate TRACE. Used with permission.|

# ACCELERATING CLIMATE ACTION WITH AI

# CO2 AI: Helping Business Ecosystems Reduce their Carbon Footprints

In order to make real progress on decarbonization, organizations need a more granular and actionable view of their carbon footprints, both across their Scope 1, 2, and 3 emissions and at the level of individual product areas. Until now, that kind of single source of truth has not been available to help operations leaders understand emissions hot spots and explore potential solutions.

CO2 AI, an innovative SaaS platform, helps organizations seamlessly map emissions across their value chains and leverage those insights to drive climate action. AI plays a central role in both assembling emissions data and matching it to activities and products—and in simulating solutions and building decarbonization roadmaps.

In one example, a global health care company seeking to reduce its Scope 3 emissions by 20% by 2030 embraced CO2 AI. The platform enabled it to incorporate 50 times more factors into its calculations and to develop an activity based emissions baseline that was 20% more precise. And CO2 AI’s simulation and roadmapping tools enabled it to identify decarbonization opportunities that would deliver 120% of its emission reduction target.

# Application area: Micro-Level Measurement

# Measuring and managing emissions with CO2 AI

# Plan reductions

Your company has 15 ongoing initiatives to reduce its footprint among which 6 in the roadmap:

|Emission scope in 2023|Roadmap target|
|---|---|
|89% of emissions come from Scope 3|Current emissions are 18% away from target|

|Scope|Scope 2|Cycle 2023|Cycle 2033|
|---|---|---|---|
|Scope 1|195.58 kt CO2e|96.97 kt CO2e|Target|
|Current cycle|Projected with initiatives|Current total| |
|2.50|0.50| | |

Scope 3: Total increase achieved from baseline

|Latest footprint|Target footprint|
|---|---|
|2.58 Mt CO2e|211 Mt CO2e|

Source: CO2 AI. Used with permission.

BOSTON CONSULTING GROUP GOOGLE

# Reduction and Removal

AI has the potential to aid organizations in reducing and removing emissions in two ways: enabling emissions reduction and supporting nature-based and technology-based carbon removal.

# Enabling Emissions Reduction

AI can contribute to the creation of more efficient and cleaner energy systems in multiple ways. It can, by consolidating information from dozens of different organizations and grid components, provide insights on how to optimize electric grid operations—and support informed decision-making on grid planning. It can also help speed transition from fossil fuels to alternative energy sources through better supply and demand forecasts that reduce the need for battery storage and standby power and enable more efficient real-time balancing of electric grids.

For example, Tapestry, an Alphabet project, is creating a single virtualized view of the electricity system with the goal of lowering emissions, minimizing outages, shortening interconnection queues, and integrating more renewables into the grid. AI is at the heart of its computational and simulation tools. Relatedly, on the subject of renewables, France’s Engie has partnered with Google Cloud to develop and pilot an AI-powered tool that can provide grid operators with more accurate real-time forecasts of wind energy supplies.9

In Africa and India, Husk Power Systems provides “pay-as-you-go” 100% renewable power to off-grid and weak-grid communities that is 30% cheaper than the alternative: diesel generation. Husk estimates that its AI model enables it to predict user demand with 80% accuracy across its microgrids, thereby improving capacity utilization, reducing costs, delivering lower prices, and guiding capital investment in additional capacity.

Moreover, AI-driven insights can also enable people and organizations to make smarter decisions that decrease emissions. For instance, as a result of using AI to improve demand forecasting, manufacturers can avoid both overproduction and the emissions those unsold goods would produce. Similarly, AI-optimized transportation can reduce emissions by identifying and directing drivers to the most efficient routes. As of September 2023, Google Maps’ fuel-efficient routing feature was estimated to have helped prevent more than 2.4 million metric tons of CO2e emissions since its launch in October 2021—equivalent to taking approximately 500,000 fuel-based cars off the road for an entire year.10

And between 2011 and 2022, Google’s Nest thermostats are estimated to have helped customers cumulatively save 113 billion kWh of energy—the rough equivalent of double Portugal’s annual electricity use—by proposing thermostat adjustments based on customer behavior, such as automatically adjusting temperatures when customers are away from home.11

In the realm of agriculture, the integration of AI tools with technologies such as drones can help farmers monitor their crops in real time for better field management, thus enhancing agricultural productivity while minimizing GHG emissions. Moreover, AI-driven precision farming helps empower farmers to make well-informed, data-driven decisions regarding farming practices, crop selection, irrigation, fertilizing, pest management, and harvesting. This approach streamlines resource utilization and, if done purposefully, can minimize the environmental impact associated with farming practices. For example, Alphabet’s project Mineral is using robotics, AI, and computer vision to create a more sustainable food production system. It is developing perception-powered solutions with partners across the agriculture value chain—from grocery retailers and enterprise farms to equipment manufacturers and crop protection companies—to develop a better understanding of the complex interactions of plants, their growing environments, and farm management practices.12

Another interesting use case involves using AI to reduce contrails. Contrails, the white clouds that sometimes form behind airplanes when they fly, are responsible for about 35% of the aviation sectors’ global warming impact. AI solutions developed by Google Research in partnership with Breakthrough Energy have enabled airline pilots in trial studies to reduce contrails by up to 54%.13 (See the sidebar The Contrails Impact Task Force: Addressing Aviation’s Other Contribution to Warming.)

# Supporting Nature-Based and Technology-Based Removal

According to the IPCC, limiting warming to 1.5°C by 2100 will require an extensive deployment of CO2 removal measures, of which there are two broad types: nature-based removal in which carbon is removed by and stored in natural sinks such as forests, algae, and wetlands, and technology-based removal via approaches such as direct air capture (DAC).14 AI can play a supporting role in both types of removal.

In nature-based removal, AI-based solutions can help quantify and verify the level of carbon sequestration achieved in an ecosystem, enabling public and private sector leaders to make informed decisions regarding the deployment of natural solutions, including land management and reforestation efforts. One actor in this space is Albo Climate. Using myriad remote sensing imagery and proprietary AI algorithms, Albo Climate monitors and quantifies environmental metrics such as above- and below-ground carbon sequestration and land-use dynamics in forestry and agricultural ecosystems and provides transparent and reliable data to various stakeholders of the nature-based markets.

# The Contrails Impact Task Force: Addressing Aviation’s Other Contribution to Warming

Aviation is one of the hardest sectors to decarbonize. According to the IPCC, contrails—the thin, white lines you sometimes see behind flying aircraft—account for roughly 35% of aviation’s global warming impact.

Contrails are created in certain atmospheric conditions that enable water droplets to condense and freeze around the soot particles from jet engine exhaust. Some dissipate quickly, while others form into persistent contrail-cirrus clouds that can last for hours, trapping heat that would otherwise escape into space.

To mitigate this, Google Research teamed up with American Airlines and Breakthrough Energy to combine AI and huge amounts of data to predict where contrails will form and how planes can avoid making them.

The trial reduced contrails by 54% across 70 live American Airlines flights. As part of the initiative, American Airlines integrated contrail-likely zones into the tablets their pilots used, enabling them to make in-flight altitude adjustments to avoid creating contrails, just as they do to avoid turbulence.

In October 2023, a new partnership was announced with EUROCONTROL’s air traffic control center that manages the airspace over Belgium, the Netherlands, Luxembourg, and northwest Germany—one of the busiest airspaces in the world. With this partnership, EUROCONTROL will be able to provide aircraft flying through its airspace with information about how to avoid making contrails.

# Application area: Enabling Emissions Reduction

|Contrails detected over the United States|2023-03-31|Dd|13:00|14:00|15:00|16:00|17:00|18:00|19:00|20:00|21:00|22:00|23:00|00:00|01:00|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |AN| | | | |
| | | | | | | | | | | |GOLs 16| | | | |
| | | | | | | | | | | | | |A0 L0JS| | |

Source: How AI is helping airlines mitigate the climate impact of contrails, Google Blog, August 2023. Used with permission.

BOSTON CONSULTING GROUP GOOGLE

In the sphere of technology-based removal, advanced technologies such as DAC can filter and capture CO2 from the air as it passes through a device. The captured CO2 can then be stored underground in, for example, saline aquifers—or prepared for industrial applications. This technology currently faces questions about its energy efficiency, which may hinder scalability, but ongoing research and development efforts may resolve these challenges. Another approach is bioenergy with carbon capture and storage, which generates energy from biomass such as wood and agricultural waste and captures the resulting CO2 for underground storage or industrial use. AI can play a role in assessing optimal capture and storage locations, monitoring for potential leaks, and optimizing the industrial processes and materials used in carbon capture.

# AI as an Enabler of Adaptation and Resilience

Even if mitigation efforts enable us to achieve the Paris Agreement goal of limiting warming to 1.5°C, communities will need to adapt and build resilience to the consequences of a warming planet. AI-driven solutions can play a critical role in two specific areas: predicting hazards and managing vulnerability.

# Hazard Prediction

Some climate impacts, such as sea-level rise, are slow moving. Others, such as flooding, are fast. The incidence of extreme weather events—for example, heatwaves, heavy precipitation, droughts, and severe storms—is increasing. A CDP analysis estimates that S&P 500 companies face a potential $40 billion to $50 billion impact from physical climate risks by 2026. In light of that, government and business leaders need to double down on preparation—and AI can make a significant difference in two areas: enabling early warning and projecting long-term trends.

# Projecting Long-Term Trends

The impacts of climate change vary across regions and cities due to the complex interplay of local geography, weather patterns, ocean currents, and other variables. AI can play a pivotal role in developing powerful climate models that can anticipate adverse impacts such as rising sea levels and drought—and assessing their implications for local communities on factors such as economic development, infrastructure, and agricultural and fishing output. These insights enable the development of thoughtful resilience strategies to mitigate the effects of climate change.

# Vulnerability Management

Prediction is undeniably a crucial aspect of preparedness; however, it should be complemented by proactive efforts at the local level to fortify communities against both sudden and protracted crises. AI is showing significant promise in helping manage crises and build forward resilience for physical infrastructure and living creatures.

# Responding to Crises

When a crisis strikes, it is incredibly valuable to have tools that help to ensure the right resources are allocated to the right tasks and in the right locations. AI can help crisis managers by combining data from scattered sources and offering a consolidated, real-time view of facts on the ground. One example is Google’s Wildfire Boundaries tracker that uses satellite imagery and AI models to detect the location of wildfire boundaries in real time and then display them in Search and Maps to support both responders and residents in making informed decisions.

Another example is in helping governments and NGOs to prepare and provide support and shelter to people displaced by extreme weather events. (See the sidebar Helping UNHCR Get Ahead of Forced Displacement in Somalia.)

# Building Early-Warning Systems

AI can save lives and minimize property damage by predicting devastating weather events and giving governments and people time to prepare. Riverine floods offer an example. Extreme rains take time to flow down river and that time can be put to good use taking action to mitigate their impact on communities along the banks. Flood Hub, an initiative of Google Research, enables governments, aid organizations, and individuals to take timely action and prepare for riverine floods via locally relevant flood data and forecasts up to seven days in advance. (See the sidebar Providing Early Warning of Rising River Levels with Flood Hub.)

# Building Resilient Infrastructure and Protecting Biodiversity

AI can also support risk assessment and remediation planning for critical infrastructure, helping localities model vulnerabilities, prioritize resilience-building investments, and pressure-test plans. In India, Google is helping the government address food and water security challenges by interpreting satellite data to track farm boundaries, measure forest and woodland acreage, and identify improvements to irrigation structures to prepare for droughts.

15 ACCELERATING CLIMATE ACTION WITH AI

# Providing Early Warning of Rising River Levels with Flood Hub

Annually, floods cause thousands of fatalities worldwide, disrupt the lives of millions, and lead to significant financial costs. They are one of the deadliest natural disasters, and climate change is increasing their frequency and severity.

Better prediction of impending flooding has the potential to save lives and mitigate the extent of property damage. Flood Hub—powered by AI models developed by Google Research—aims to predict when and where riverine flooding will occur in order to provide timely warnings to governments, organizations, and the people likely to be affected, empowering them to act before the flood strikes.

Real-time flood forecasts and visualizations are available on the Flood Hub platform and, in many cases, also on Search and Maps. As of 2023, Flood Hub covers more than 80 countries, providing forecasts up to seven days in advance. It offers alerts for geographies across Africa, Europe, South and Central America, and the Asia-Pacific region that combined are home to 460 million people. In October 2023, Flood Hub expanded to the US and Canada, covering more than 800 riverbanks where over 12 million people live. The goal is to bring flood forecasting to every country and to include more types of floods through ongoing collaborations with governments, communities, academics, and organizations such as the World Meteorological Organization.

# Application area: Early Warning Systems

Flood Hub’s heat map of flood risk

Source: Google. Used with permission.

BOSTON CONSULTING GROUP GOOGLE

# Helping UNHCR Get Ahead of Forced Displacement in Somalia

Millions of people in Somalia face displacement as a consequence of climate-driven natural disasters, resource shortages, and violent conflict. In 2022 alone, climate-driven events—drought, floods, wildfires, and storms—displaced 1.2 million Somalis, representing nearly two-thirds of all internal displacements for the year. On point to support those refugees, UNHCR, the United Nations’ refugee agency, wanted a better way to forecast where and when to deploy its resources.

It partnered with Omdena, a global, crowdsourced community of AI experts, to develop AI solutions that could predict displacement a month in advance. Omdena developed machine learning models that helped predict areas for intervention based on identified conflict “hot zones” combined with drought and agricultural production metrics. The insights from these models are enabling UNHCR to optimize the assignments of its personnel and deployment of resources.

# Application area: Adaptation and Resilience

17

# ACCELERATING CLIMATE ACTION WITH AI

Moreover, AI can help people understand and mitigate the impacts of a warming planet on agriculture, fisheries, and the broader natural world. In agriculture, it can control intelligent irrigation systems, identify early signs of crop diseases, predict future yields based on current trends, and promote knowledge transfer across biomes. It can also help protect wilder places. Global Forest Watch, for example, uses AI and satellite imagery to create a real-time tool to monitor and combat deforestation.

# AI’s Foundational Capabilities to Support Climate Action

AI can also help turbocharge foundational capabilities that are essential to shaping an effective response to the climate crisis.

# Climate Modeling

AI can strengthen climate models by filling in data gaps, enabling the incorporation of additional variables, and navigating data sets too large for human analysis. It can also yield more accurate estimates by modeling multidimensional complex systems and the feedback loops among, for example, climate and socioeconomic variables. The greater accuracy and precision of the AI models in turn enhances the impact of AI-supported climate applications.

# Climate Economics

AI can improve estimates of the financial implications of climate-related impacts and response measures, enabling policymakers and private-sector leaders to better understand which investments today are likely to yield the greatest benefit. For example, government leaders in Lagos, Nigeria—one of the African continent’s most vulnerable cities—leveraged AI to model the potential financial and socioeconomic impacts of rising sea levels and evaluate those investments with the highest impact on adaptation and resilience. (See the sidebar Helping Lagos Shape Its Strategy for Climate-related Adaptation and Resilience.) Another example is Sprout, an insurtech startup that provides coffee farmers with crop insurance based on weather fluctuations. (See the sidebar Sprout: Helping Smallholder Coffee Farmers Navigate Climate Change.)

# Education and Behavioral Change

AI can help influence climate-friendly behavior. After all, people may wish to make climate-friendly choices but lack the information to know, for example, the relative carbon footprint of two pairs of jeans. By providing relevant information, AI can help consumers make environmentally conscious choices. For example, Google Maps uses AI to suggest fuel-efficient routes that have fewer hills, less traffic, and constant speeds with the same or similar ETA. The feature is available in the US, Canada, Europe, and Egypt and will be rolling out in India and Indonesia during 2023. In India and Indonesia, the feature will be expanded to two-wheelers, helping even more people to travel more sustainably.

# Innovation and Breakthroughs

AI can also accelerate breakthrough innovation in domains that could open new frontiers in the battle against climate change. For instance, in the field of material science, AI has already aided the discovery of a new family of solid-state materials that conduct lithium. These solid electrolytes will be helpful in the development of solid-state batteries that offer longer ranges and increased safety for electric vehicles. In the field of clean energy, Google DeepMind has pioneered a deep reinforcement learning system that helps researchers better control nuclear fusion plasma, opening new avenues to advance fusion research and thus clean energy alternatives. (See the sidebar Accelerating Fusion Science through Better Plasma Control.)

I is clearly poised to play a pivotal role in shaping positive climate outcomes. But, alongside its benefits, it is crucial to also acknowledge the potential risks associated with its implementation. The next chapter offers some perspective.

BOSTON CONSULTING GROUP GOOGLE 18

# Helping Lagos Shape Its Strategy for Climate-Related Adaptation and Resilience

Lagos is one of Africa’s most populous urban areas. It is also home to the continent’s fourth-busiest port and contributes around 30% of Nigeria’s GDP. At an average elevation of only 1.5 meters above sea level—and with much of the city at or below sea level—it is also one of the cities most endangered by rising sea levels.

But Lagos has set itself on a journey to build a more resilient future, leveraging data and analytics to build a robust adaptation and resilience plan that addresses the impact of extreme weather on its key systems. The plan is guiding the city to mobilize financing and implement effective governance, legislation, and monitoring capabilities.

AI-enabled tools have played a central role in guiding Lagos’s journey—first, in risk assessment and then in shaping and prioritizing strategies. Lagos’s risk assessment was based mainly on four key indicators: flood intensity, capital cost to damaged infrastructure, impact of extreme events on GDP, and the number of citizens affected. The data is calibrated in increments of only 500 square meters—small enough to show fine-grained patterns of climate vulnerability. Overall, the model estimated 165 square kilometers would likely be inundated, 700,000 residents would need to be relocated, and there would be $5 billion in damage to transport, communications, and power infrastructure. The heat map below shows the model’s prediction of inundation risk, with the red areas the most vulnerable.

These AI-powered tools then enabled Lagos’s leaders to simulate the relative contribution of different strategies under multiple scenarios. It also helped estimate the cost of inaction, which, at about $30 billion, represents 12 times the budget of the Lagos metropolitan area.

By utilizing these tools, policymakers have curated a prioritized portfolio of projects spanning three broad areas. One of these areas concentrates on enhancing infrastructure resilience, exemplified by initiatives such as the construction of an 18 km embankment and sea walls designed to safeguard more than 2.7 million individuals, including 700,000 from vulnerable populations. Another revolves around bolstering community resilience and safeguarding vulnerable groups, with initiatives such as the establishment of infectious disease surveillance systems. And the third factor centers on proactively addressing risks and enhancing crisis response capabilities, such as the establishment of well-defined post-disaster procedures.

The city has actively engaged with a diverse array of stakeholders from the public, private, and social sectors. Currently, it is in the process of implementing its Climate Adaptation and Resilience Plan while securing funding from various sources including the private sector, public sector, NGOs, and others.

# Application area: Climate Modeling, Climate Economics, and Adaptation and Resilience

# Inundation risk heat map for Lagos

Source: BCG Climate Impact AI Platform.

19 ACCELERATING CLIMATE ACTION WITH AI

# Sprout: Helping Smallholder Coffee Farmers Navigate Climate Change

Coffee production faces a significant threat from the extreme temperatures and unpredictable rainfall that are a result of climate change. Small farms are particularly vulnerable. And many are seeing declines in yields of up to 15% as a consequence—yet few have access to or can afford crop insurance.

Sprout, an insurtech startup, offers an innovative, AI-driven solution that helps farmers navigate risks and withstand full or partial crop failures resulting from extreme climate conditions. Sprout brings its own proprietary data on coffee farming together with data from satellites and other sources to do two things that support smallholder farmers.

First, via the Sprout mobile app, it offers locally customized agronomy advice to farmers on how best to navigate unexpected weather trends. This reduces intra-seasonal risks, thereby requiring less insurance cover. Second, via an innovative index insurance offering, Sprout helps alleviate downside impacts. Premiums are paid by the farmers’ direct customers—and ultimately by developed-world coffee consumers. Index insurance doesn’t require farmers to file claims to receive compensation. Instead, it provides automatic payouts should an index variable for the local area (for example, rainfall) fall below a target value. Sprout is piloting its Climate Smart CoffeeTM program with support from USAID Development Innovation Ventures in Kenya.

Sprout aspires to offer protection to over 1 million farmers worldwide by 2030.

# Application area: Climate Economics

# Sprout’s AI-enabled crop insurance offering

|Sprout Crop Map|Preose Climate Data|
|---|---|
|Using Machine Learning and Sprout coffee farm data|Filtered through our Crop Map|

# Index Insurance Product

Specifically to cover extreme weather events

Source: Sprout. Used with permission.

BOSTON CONSULTING GROUP

GOOGLE

20

# Accelerating Fusion Science through Plasma Control Simulation

Nuclear fusion has the potential to be a source of abundant, clean energy. It is the reaction that powers the stars of the universe. But huge breakthroughs will be required for it to become cost effective and scalable. A critical aspect of fusion research involves learning how to control and sustain a hydrogen “plasma” that is hotter than the core of the sun. One tool researchers use is a tokamak, a doughnut-shaped vacuum that aims to contain the plasma by making thousands of adjustments per second to a set of powerful magnetic coils. The magnets seek to keep the plasma from touching the vessel walls, which would, at a minimum, dissipate heat, or worse, damage the tokamak. Since the world’s tokamaks are in high demand, one way to advance and accelerate fusion research is through simulation.

A collaboration of Google DeepMind and the Swiss Plasma Center at EPFL, a Swiss research university, has leveraged AI to create the first deep reinforcement learning system for fusion research. It simulates EPFL’s Variable Configuration Tokamak (TCV) and has successfully modeled ways to stabilize and sculpt plasma that have subsequently been validated in the actual TCV—opening new avenues to advance nuclear fusion research.

# Application area: Innovation and Breakthroughs

# Navigating AI’s Potential Risks

As governments and businesses increasingly rely on AI to help mitigate emissions, build resilience, and adapt to a changing climate, a critical question arises: what risks are associated with the rise of AI? Understanding and navigating these risks is essential if we are to scale AI responsibly and manage its environmental footprint. GHG emissions, water, and waste management are three key areas that will be addressed in this chapter.

# Issue 1: AI’s Energy-Related GHG Emissions

In 2022, global data center electricity consumption accounted for 1.0% to 1.3% of global final electricity demand. Further, a 2022 paper in Nature Climate Change estimates that cloud and hyperscale data centers are responsible for 0.1% to 0.2% of global GHG emissions and that roughly 25% of their workloads are related to machine learning. A critical question is how—with AI at the start of a new innovation and adoption curve—data center electricity use and related GHG emissions will evolve going forward. There is a critical need for more deep research on this topic, but at this stage, we can make some important observations.

BOSTON CONSULTING GROUP

GOOGLE

Historically, data center energy consumption has grown much more slowly than demand for computing power. Between 2015 and 2018, for example, the IEA reports that data center electricity use was flat despite a doubling of compute demand and tripling of internet traffic. Furthermore, a paper in Science reports that between 2010 and 2018—a period during which data center compute demand increased sixfold and internet traffic tenfold—data center electricity use grew just 6% as a result of a shift from inefficient on-premises data centers to the highly energy-optimized cloud. And we still have optimization potential in the future. In 2022, the average annual power usage effectiveness for Google’s global fleet of data centers was 1.10, compared with the industry average of 1.55.

Looking forward, Exhibit 4 illustrates the key drivers of AI’s electricity use and GHG emissions throughout its life cycle. At the level of the grid, emissions will be determined by the power sources selected to power a data center and the efficiency of the distribution system. Compute machines and data center design choices also can have a powerful influence. The choice of more energy-efficient servers optimized for AI models can make a significant difference. AI model developers can be more mindful of the energy intensity of their programming choices. And a critical unknown is how quickly and how much end-user demand for AI-enabled products and services increases compute demand.

So how might these factors evolve? A 2022 paper by researchers from UC Berkeley and Google, which studied the energy requirements for machine learning training, identifies four best practices with the potential to reduce energy use and emissions. Let’s take each in turn:

- Energy Source Carbon Intensity. In data center emissions profiles, such as in real estate, location matters. In 2022, Norway’s electric grid had an average carbon intensity of 29 g CO2e/kWh, compared with an average of 102 in Brazil, 367 in the US, 489 in Singapore, and 709 in South Africa. And even within a country, the share of carbon-free energy can vary significantly from region to region—meaning that many organizations operate in jurisdictions without easy access to clean energy. And while trade associations such as the Clean Energy Buyers Association, RE-Source, and the Asia Clean Energy Coalition are working to increase access, changes are still needed.
- Other choices matter too. Information and communications technology (ICT) companies have led the world in adopting renewable energy power purchase agreements (PPAs), with Amazon, Microsoft, Meta, and Google having signed renewable energy agreements totaling almost 50 GW of clean energy generation capacity through 2022, equal to the generation capacity of Sweden. And many tech leaders are going further. Google, for example, has a target to run on carbon-free energy in every grid where it operates by 2030, is already procuring energy from geothermal power plants and battery-based backup power systems, and is piloting the use of AI algorithms to better predict wind production and facilitate its integration into the grid.

# Exhibit 4 - Critical factors determining AI’s emissions footprint

|AI-related energy flow|Power plants|Energy distribution|Data center operations| |Developers|End-user demand for AI-enabled products|
|---|---|---|---|---|---|---|
|Energy source|Carbon intensity|Data center infrastructure|Model development|&amp; coding|AI adoption|&amp; usage|

Source: BCG analysis.

23 ACCELERATING CLIMATE ACTION WITH AI

# Data Center Infrastructure

Data center energy needs are driven by server and infrastructure choices. Servers specifically designed for machine learning can run AI models faster while using less power. But servers aren’t the only source of energy demand. Additional power is needed to operate the facility—for example, for cooling and lighting. And specific data center equipment choices matter. A study by researchers at Berkeley and Google finds that Google owned, designed, and operated cloud data centers, for example, can be ~1.4–2.0 times more energy efficient than traditional data centers, and hardware specifically designed to support AI and machine learning can be ~2–5X more efficient than off-the-shelf systems. 29 Google’s machine-learning optimized Tensor Processing Units (TPUs) are an example: TPU version 4 has proven to be one of the fastest, most efficient, and most sustainable machine learning infrastructure hubs in the world with the potential to generate 93% fewer emissions compared with unoptimized servers using P100 GPUs. 30

However, new processors require new manufacturing practices and therefore attention must be paid to their embodied carbon. Future hardware design should look at optimizing full life cycle, instead of just operational, GHG emissions. And relatedly, more effort is needed from the semiconductor industry to understand and reduce embodied emissions.

# Model Development and Coding

State-of-the-art approaches to developing AI models are varied and evolving, but one thing is clear: the desire for more precise and accurate model outputs has been leading to more complex models that rely on larger sets of training data and require more processing power. 31 These more complex models may lead to higher energy consumption, all other factors being equal. Nonetheless, it is important to note that AI model design is an evolving field, and new releases and versions of complex models consistently demonstrate improved energy efficiency while maintaining model performance. Indeed, ongoing improvements in software and algorithmic optimization have the potential to significantly enhance efficiency and decrease computational requirements. One example is the development of evolved sparse models for deep neural networks, which can reduce computations by approximately 5 to 10 times while maintaining the same level of output quality compared with denser baseline models. 32

# Adoption and Usage

AI use is forecast to grow. In an IBM Global survey, 35% of companies reported already using AI in their business in 2021, with an additional 42% stating that they are piloting AI applications for later adoption. 33 Some of the growth in AI adoption might replace existing workloads in today’s data centers, but given the expansion of use cases, aggregate demand will grow. At present, however, there is no recent, peer-reviewed research that forecasts future AI workloads and energy needs.

Any AI model has two phases to its life cycle: training and inference. Training gives the model its smarts and happens sporadically, while inference is the production phase in which the model is used by customers. Inference workloads are therefore driven by customer adoption and usage. And today, inference processing accounts for 80%–90% of AI and machine learning workloads. 34

These factors are synthesized in Exhibit 5, which makes a critical point: while there is uncertainty on future AI emissions, our decisions matter. We are not suggesting that these are equally important, only making the point that already today there are technology, architecture, and location options that can significantly mitigate AI’s GHG impact.

And, beyond these active measures, there are other factors that will influence the speed and scale of AI deployment (for example, the economics of data center development). Data centers can take years to build and require significant capital investment.

# Issue 2: AI’s Water Use

Data centers generate insight, but they also generate heat. This heat must be dissipated to protect the servers, communication equipment, and storage devices they contain. For warehouse-scale data centers, water-based cooling is the most common approach. And among water-cooling solutions, evaporative cooling—in which water absorbs ambient heat through evaporation—is frequently both the cheapest and the most energy efficient. Google found that its water-cooled data centers use about 10% less energy than its air-cooled data centers. 35 But water cooling has the potential to exacerbate pressure on water resources in specific locations. A Virginia Tech study estimates that one-fifth of US data centers (primarily located in Western states) draw their water from moderately to highly stressed watersheds. 36

BOSTON CONSULTING GROUP GOOGLE

# Exhibit 5 - Critical choices can shape AI’s emissions footprint

|Factor and Baseline Metric|Reduced emissions|Increased emissions|
|---|---|---|
|AI adoption & usage|–100%|Unknown|
|Baseline: Current AI compute consumption| | |
|Model development & coding|–80%|90%|
|Baseline: Transformer (2017)| | |
| |Evolved (2019) and Primer (2021) models| |
|Data center infrastructure (servers)|–93%|–23%|
|Baseline: Unoptimized systems energy use|(P100 from 2017)| |
| |ML-oriented1|ML-oriented1|
| |(TPU v4, 2021)|(TPU v2, 2019)|
|Data center infrastructure (non-IT equipment)|–30%|50%|
|Baseline: Traditional data center energy needs| | |
| |Cloud data centers| |
|Energy source carbon intensity3|–94%|–77%|
| |–22%–16%|+12%|
| | |+60%|
|Baseline: Global grid emission intensity in 2022| | |
| |Norway|Brazil|
| |FLAP-D4US|Singapore|
| |South Africa| |

Note: The figure is based on the most recent data available on actual emissions profiles for different choices—and is not intended to suggest that these factors are equally important.

1Patterson, D. et al., 2021. Carbon Emissions and Large Neural Network Training.

2Patterson, D. et al., 2022. The carbon footprint of machine learning training will plateau, then shrink.

3Energy Institute Statistical Review of World Energy.

4Europe Data Centers main locations: Frankfurt, London, Amsterdam, Paris, and Dublin.

In the data center sector, water use is not widely reported—and actual volumes will vary widely based on the center’s size, location, local weather conditions, and the use of its infrastructure. A 2016 study from the US Department of Energy estimates data center water consumption at 1.7 billion liters/day, of which 0.3 billion liters/day is used on site for cooling, or 0.02% of total US water consumption of 1,218 billion liters/day.

Clearly, data center operators need to be mindful of and manage a tradeoff between energy use and water use. Google began disclosing water use for each of its owned US data center locations in 2021 and for global owned data center locations in 2022. A Google analysis of the 2021 data finds that its embrace of water cooling across its data centers reduced its carbon emissions by roughly 300 kilotons—the emissions equivalent of about 64,000 passenger vehicles. The 5.2 billion gallons of water required to do that in 2022 was comparable to the water needed to irrigate 34.8 of the more than 11,000 golf courses in the United States or the annual water consumption of 69,800 average American homes.

Tech players are also starting to explore new, more water-efficient approaches. In a data center, temperature, airflow, and relative humidity (RH) are the three critical factors to manage. Based on guidance from the American Society of Heating, Refrigerating, and Air-Conditioning Engineers, Meta has experimented with shifting the lower-bound for RH in its data center from 20% to 13%. The nine-month pilot yielded water savings of 40%.

Data center operators are also taking steps to replenish their water consumption. Google, for example, has a target to replenish 120% of the freshwater volume it consumes on average by 2030 through initiatives including wetland restoration, rainwater harvesting, and land conservation.

# Issue 3: Waste

The United Nations estimates that globally 53.6 million metric tons of electronic waste was generated in 2019. This figure represents a 21% increase in just five years. And the volume is projected to increase to 74.7 million metric tons by 2030—representing a near doubling of e-waste over a 20-year period.

While there is currently a lack of specific data regarding e-waste generated by data centers, they clearly only account for a fraction of the broader e-waste challenge. Nonetheless, there is a clear imperative for tech firms to take a smarter, more circular approach to waste.

Circular economy principles emphasize the opportunity to maximize the lifespan of products and materials through practices such as reuse and recycling. For tech companies, this entails designing products and data center infrastructure with an eye toward longevity and ease of upgrading or repurposing. Moreover, it involves establishing efficient systems for recycling and refurbishing electronic equipment, ensuring that valuable materials are reclaimed and that hazardous substances are disposed of responsibly.

Microsoft’s Circular Centers, for example, focus on finding productive uses for decommissioned equipment, including new homes for older equipment, such as in schools. They break servers down into components that can be reused by others, and return other items to suppliers for recycling and reclamation. The first of these centers opened in 2020 in Amsterdam and has been able to channel 83% of e-waste into reuse—and 17% into recycling. Based on that initial success, five other Circular Centers were established in 2022.

# Other Potential Risks

The rise of AI also brings a set of societal and ethical risks that must be managed vigilantly. It is important to have a set of clear principles that guide the development and use of AI. For example, Google has outlined the following seven key principles for its development of AI applications:

1. Be socially beneficial
2. Avoid creating or reinforcing unfair bias
3. Be built and tested for safety
4. Be accountable to people
5. Incorporate privacy design principles
6. Uphold high standards of scientific excellence
7. Be made available for uses that accord with these principles

# Application Selection and Optimization Metrics

There are any number of climate-unfriendly applications to which AI could be applied, for example, oil and gas exploration. Google, for instance, has pledged not to develop customized AI/machine learning solutions to facilitate upstream extraction for oil and gas. In addition, algorithms could be designed to optimize for financial or other outcomes over environmental ones. For example, travel website algorithms could steer customers to the cheapest flights regardless of carbon emissions instead of guiding them toward an informed compromise between price and emissions.

In 2016, Google announced a “Zero Waste to Landfill” goal for its data center operations, which it defines as more than 90% of waste diverted from landfill. In 2022, 38% of Google owned and operated data centers had achieved Zero Waste to Landfill.

Other firms—for example, Iron Mountain through its 2021 acquisition of ITRenew, which specialized in refurbishing and repurposing used data center equipment from hyper-scale operators—are pursuing circularity as a business opportunity.

It is also important to guard against unintended consequences. While AI can help optimize resource use and curtail emissions, there are scenarios in which it could influence consumer behaviors that lead to unintended increases in emissions. For instance, AI-powered autonomous vehicles and smart transportation systems can optimize routes and reduce fuel consumption, but their convenience could lead to increased vehicle use, which could potentially increase overall emissions if the vehicles are not predominantly electric or powered by renewable energy sources.

Looking beyond the risk of negative environmental impact, we must guard against unethical applications, for example, the spreading of misinformation and disinformation.

BOSTON CONSULTING GROUP GOOGLE

# Equity and Bias

Clearly, AI models need to be trained on diverse data sets that reflect the world’s range of people to ensure both fairness and the accuracy of model output. And beyond that, it is essential that we take positive steps to ensure that the growth of AI does not exacerbate regional disparities. Today, the majority of advanced climate modeling and AI development occurs in the Global North. This divide arises from several factors, including the Global North’s more extensive technological infrastructure that allows for richer data collection—for instance, through satellites and drones—and its greater computing power. Additionally, AI expertise and resources tend to be more readily available in these affluent regions when compared with the Global South.

# Privacy and Security

The large data sets that train AI algorithms will at times include personal data. It is essential to ensure that AI applications are aligned with established privacy standards and regulations to protect individuals.

Given the promise of AI to address the climate crisis, policymakers will want to encourage its use—but also mitigate its potential risks. The next chapter offers a summary of critical policy outcomes.

However, the concentration of AI development and application in certain regions has significant repercussions. Climate AI models primarily trained on data from the Global North may inadvertently neglect vital information about the Global South, with its distinct climate patterns, vulnerabilities, and emissions sources. A Google Research team in Ghana, for example, is focused on leading many sustainability initiatives of particular interest to Africa in collaboration with local universities and research centers. Additionally, historical data often mirrors emissions and climate impacts in more industrialized regions, further skewing data representation. When such biased AI models inform climate assessments or policymaking for the Global South, they risk yielding flawed and inaccurate outcomes. Excluding specific regions or historical periods can result in inaccurate predictions and evaluations of carbon emissions, environmental consequences, and climate trends in these underserved areas. This undermines climate science accuracy and obstructs effective decision-making and planning for climate adaptation and mitigation in the Global South.

27 ACCELERATING CLIMATE ACTION WITH AI

# AI for Climate

# A Summary of Critical Policy Outcomes

Policymakers play a central role both in harnessing the potential of AI for climate action and in ensuring its sustainable and equitable use.

In this chapter, we share a set of suggestions for policymakers that synthesizes the convergences and complementarities across more than 30 expert interviews and a comprehensive review of the literature (See the References section for more detail). We also draw on best-practice approaches from related policy domains such as energy, transport, and buildings.

# Policy can make a difference in ensuring and accelerating the following three critical outcomes:

- Enabling the use of AI for climate action by building awareness and ensuring equal access to data, technology infrastructure, and talent around the globe
- Deploying public-sector solutions on priority use cases while catalyzing private sector action through the right incentives
- Promoting the responsible use of AI in climate action, taking into account its potential environmental as well as social impacts

BOSTON CONSULTING GROUP GOOGLE

Exhibit 6 offers a menu of possible policy moves in support of these desirable outcomes. The rest of the chapter provides examples of how policymakers—as well as business and social-sector leaders—have already taken steps to contribute to these outcomes. While policy priorities must be tailored to the specific circumstances and capabilities of each country and region, we believe all leaders should adopt clear AI principles to ensure the responsible development and application of the technology.

We expand on the thinking in the remainder of the chapter, and hope our framing provides inspiration and a starting point.

# Enable AI for Climate

If we are to be successful in maximizing AI’s contribution to climate action, one critical area for policy focus is on the supply side, ensuring that AI’s critical inputs—high-quality data, technology infrastructure, and talent—are available wherever needed. We discuss each in turn.

# Encourage Data Collection and Sharing

AI impact starts with good data. Without it, algorithms cannot generate accurate and effective insights or recommendations. Actionable wildfire alerts, for example, cannot be developed without access to high-quality, real-time satellite data—and good agricultural advice is impossible if data is available only for a limited number of crops or geographies. Moreover, to yield useful insights, many AI applications for climate will need to tap into multiple data sources. London Transport, for example, leverages data on emissions sources, road traffic, air quality, and population density to monitor air pollution challenges and identify highly exposed locations. Making the data available is not enough; it also needs to be accessible in standard formats that allow data from different sources to be merged safely and efficiently.

It is therefore essential that policymakers take steps to make data accessible—at a minimum in the climate sphere, given the urgent need for rapid and effective action to reduce emissions and build resilience globally—while also protecting trade secrets and intellectual property.

# Exhibit 6 - AI for Climate: A summary of critical policy outcomes

|Policy outcomes|Enable AI for climate|Deploy AI for climate|Guide AI for climate|
|---|---|---|---|
|Ensure the availability of data, technology infrastructure, and talent|Drive AI solutions for climate in public sector—and catalyze private sector action|Promote environmentally and socially responsible use of AI| |
| |Encourage data collection and sharing|Define and deliver on public sector priorities|Shape and execute AI for climate strategies and demonstration cases|
| |Address environmental impacts of AI operations|Enhance transparency and streamline the adoption of sustainable AI practices| |
|Ensure technology access and affordability| |Encourage private sector adoption|Create incentives to accelerate use of AI for climate|
| |Cultivate awareness and build expertise|Invest in knowledge and talent to drive AI for climate solutions|Promote socially responsible use of AI for climate|
| |Encourage fairness, inclusiveness, safety, and data privacy| | |

Source: BCG analysis.

29 ACCELERATING CLIMATE ACTION WITH AI

# Leaders could:

Encourage collection and sharing of climate-related data and tools across public and private organizations.

# Examples:

- The UK Climate Change Statistics Portal gives open access to climate-related data and statistics (weather, emissions of GHG, status of surface water, renewable energy share, etc.). This data is compiled from various government departments, agencies, and public bodies.
- The US Climate Resilience Toolkit, developed by a collaboration of multiple federal agencies and organizations led by the National Oceanic and Atmospheric Administration, provides essential climate information, projections, and tools to help organizations enhance their resilience to climate-related challenges.
- Sign Smart, also known as the National Greenhouse Gas Inventory System, is an application system developed by the Indonesian government. Its objective is to provide valid, accurate, and up-to-date data and information about GHG emissions, while also enhancing the effectiveness of data processing and GHG estimation at the national, provincial, and district/city levels.
- Data Commons is an initiative led by Google designed to centralize and streamline publicly available data from diverse sources. It provides a wide range of climate and sustainability-related data, covering areas such as emissions, natural disasters, and waste. Accessing this data is made simple through an interface that supports natural language searches. The AI-driven query function retrieves results directly from Data Commons, providing links to the original sources of information and data.

# Define standard processes and protocols for climate-relevant data gathering and sharing to ensure data is robust, trustworthy, safe, and respectful of privacy.

# Examples:

- The European Space Agency’s Climate Change Initiative (CCI) aims to deliver a consistent, satellite-derived data set of Essential Climate Variables (for example, greenhouse gases, sea level, glacier status, etc.) to aid climate modelers and researchers over the long term. To guarantee consistency among the various projects within the program, it has released data standards outlining the minimal requirements for climate data producers.
- The World Meteorological Organization has published the Technical Regulations, an international framework for data standardization and interoperability in the fields of meteorology, hydrology, climatology, and related environmental disciplines. These standards enable the continuous operation of global systems, ensuring 24/7 observations, data exchange, management, forecasting, and the delivery of authoritative scientific assessments and standardized services.

# Create data catalogs across priority sectors for all climate-relevant data categories (for example, weather, water, agriculture, energy use, and socioeconomic factors).

# Examples:

- The World Meteorological Organization has not only published a set of data standards but also a Catalogue for Climate Data, a curated listing of global, regional, and national data sets of climate-related data that meet its standards for data quality and stewardship.
- Climate Change AI, a nonprofit, has published the CCAI Dataset Wishlist that enumerates currently unavailable data that could accelerate AI-driven climate progress. It classifies desirable data by topic as well as by its current state of availability (for example, public data needing structure, private data needing release, scattered data needing collation, and scarce data needing collection).

BOSTON CONSULTING GROUP GOOGLE 30

# Ensure Technology Access and Affordability

Without devices collecting data from the real world (for example, sensors, drones, and satellites)—and without connectivity (for example, fiber and 5G) and computing infrastructure (for example, cloud data centers)—AI algorithms are powerless. Consider an application such as AI-driven smart irrigation. Field sensors need broadband to send data to servers and storage devices in the cloud. The servers then process the data, comparing it with insights from a training set, and formulate recommendations that need to be communicated back to the irrigation system in the field.

This critical technology infrastructure, while widely available in the developed world, is not currently accessible in many less-developed regions, particularly the Global South. Affordability is also a concern. For example, customers in less-developed countries pay 6% of per capita gross national income for mobile broadband service, while those in high-income countries pay just 0.4%.47

# Leaders could:

# Build private-public partnerships to ensure affordable access and deploy locally or regionally critical AI technology infrastructure (for example, cloud data centers, satellites).

Examples:

- Japan’s Ministry of Economy, Trade, and Industry is partnering with Sakura Internet to expand Japan’s computational capacity. It is providing half of the needed investment to build an AI supercomputer, aiming to accelerate AI development and implementation in Japan.
- The European High-Performance Computing Joint Undertaking—a €7 billion initiative over 2021–2027 to build petascale and pre-exascale supercomputing infrastructure in Europe—aspires to accelerate European innovation by expanding access to state-of-the-art tools.
- The US Community Infrastructure for Research in Computer and Information Science and Engineering (CIRC) program seeks to increase researcher access to critical technology infrastructure by funding the development and improvement of top-tier research infrastructure.

# Empower the private sector to build and/or expand AI technology infrastructure.

Examples:

- Norway’s data center strategy, introduced in 2018, features public investments in fiber infrastructure as well as tax incentives (such as property tax reductions) aimed at attracting data center operators and ensuring the accessibility of computing infrastructure.
- The South African government aims to launch a National Cloud and Data Policy. This initiative—currently under consultation—seeks to provide policy certainty for investments in data centers and cloud services and to reinforce South Africa’s leading position in Africa. The draft policy includes provisions for establishing a Special Economic Zone for Digital and ICT, as well as policies addressing data protection, data localization, and cross-border data transfers.

# Support R&D for AI technology infrastructure across the public sector, private sector, and academia.

Examples:

- The US Networking and Information Technology Research and Development (NITRD) program is a federally funded R&D initiative focused on advanced IT, covering computing, networking, and software nationwide. Its 25 member agencies invest about $9.6 billion annually in various R&D programs, including high-capability computing systems, advanced communication networks and systems, and more.
- The Quantum Technologies Flagship is a 10-year, €1 billion EU initiative that aims to advance Europe’s leadership in quantum technologies by bridging research with practical applications. It brings together research institutions, industry partners, and public funders.

# Cultivate Awareness and Build Expertise

People need to remain at the center of policy and climate action. They must be aware of AI’s potential and support its use for climate action—and people with AI skills will be needed to help address the climate challenge.

It is important to build awareness among all stakeholders—policymakers, corporate decision-makers, civil servants, and the broader public—of AI’s potential contributions to climate solutions as well as of its risks. With awareness of the challenges, of key achievements, and of best practice comes support for AI-enabled climate action.

Translating that support into climate progress will require, in addition to more AI computing infrastructure, more talent. Without technical experts such as data scientists—and domain experts such as climatologists and climate economists—it will be impossible to develop, deploy, and govern climate-related AI applications. In a recent BCG survey, 78% of business leaders with responsibility for climate, AI, or both cited insufficient access to qualified talent as a barrier to using AI to address their climate-related challenges. And critical talent is not only in short supply, but also heavily concentrated in the developed world. According to the OECD’s AI Policy Observatory, North America is home to 30% of the world’s data scientists and machine learning experts, while sub-Saharan Africa hosts under 2%.

# Leaders could:

Establish AI and climate training and literacy programs for policymakers and the broader public sector workforce.

# Examples of AI-related trainings:

- Government AI Campus, created by Google.org and the Rockefeller Foundation, is an online career-development initiative for government staff that prepares them to lead in the age of AI.
- AI4Gov—a European Union-funded masters degree program offered by four leading universities, focuses on AI’s public sector application. It is part of a broader European initiative to create AI-related masters programs to build skills in areas such as AI ethics and AI’s application to health care.
- The UNESCO-developed Artificial Intelligence and Digital Transformation Competency Framework provides guidance on the essential AI and digital competencies for civil servants. This initiative responds to a significant demand for efforts to enhance the digital skills of government officials, particularly in Africa. UNESCO conducted workshops in Africa and India to gain a deeper understanding of the challenges before formulating its solutions.

# Examples of climate-related trainings:

- The UN Climate Change Learning Partnership (UN CC:Learn) offers a range of introductory and advanced online courses for policymakers to learn how to address climate change and apply an integrated approach to climate action throughout the various stages of the policy cycle.
- Climate Change and Energy: Policymaking for the Long Term is an executive education program for policymakers developed by Harvard’s Kennedy School of Government. It seeks to equip them with the knowledge, analytical tools, and frameworks needed to comprehend climate science and economics—and to craft policies and adaptation strategies.

BOSTON CONSULTING GROUP GOOGLE

# Support the creation and expansion of AI and climate-related upskilling programs for corporates

(for example, climate change training for AI experts, AI introduction for climate experts).

# Example of AI for Climate trainings:

The Climate Change AI summer school aims to equip individuals who have a background in AI and/or climate change with the knowledge and skills necessary to address significant climate challenges using AI.

# Examples of AI-related trainings:

Quebec’s Ministry of Employment and Social Solidarity has granted $23.4 million in funding to SCALE AI to upskill over 25,000 professionals, executives, and managers in AI between 2019 and 2023.

The EU-funded project Artificial Intelligence Skills Alliance (ARISA) unites 20 partners for a four-year period (2022–2025) to create the European strategy for AI skills development, including up/reskilling curricula and learning programs.

# Examples of Climate Change trainings:

Climate-KIC, a knowledge and innovation community supported by the European Institute of Innovation and Technology, provides education programs, at the intersection of zero-carbon, climate resiliency, and innovation, in Europe and online for postgraduates and professionals.

The national business support agency of Ireland, Skillnet, offers the Climate Ready Academy to help Irish businesses develop climate-related skills, including sector-specific programs such as the Energy Leaders Programme.

# Build AI and climate modules within education curricula

(for example, early-stage initiation for K-12, cross-skills for AI students or climate students, etc.).

# Examples of climate-related curricula:

Since September 2020, Italian students in every grade have spent 33 hours each year learning about climate change and sustainability, bringing Italy to the forefront of environmental education worldwide.

In the US, the National Oceanic and Atmospheric Administration’s Collection of Climate and Energy Educational Resources (CLEAN) provides open access to over 700 validated, ready-to-use teaching materials and guidelines suitable for secondary through higher education classrooms.

# Examples of AI-related curricula:

Countries such as Finland, the UK, Japan, and Singapore have introduced computational thinking and programming to pedagogical courses to increase students’ exposure to coding and computing at early stages of education.

Morocco’s Ministry of Higher Education, Scientific Research, and Innovation has initiated the “Code 212” project, designed to help students acquire skills in coding, programming, big data, AI, and related fields. A core objective is to establish Code 212 centers in all national universities, thereby enhancing students’ digital competencies alongside their specialized studies.

33

# ACCELERATING CLIMATE ACTION WITH AI

# Deploy AI for Climate

While enabling AI is necessary to help society mitigate and build resilience to climate impacts, policymakers can play an important role in accelerating the deployment of AI technologies in both the public and private sectors. We discuss each in turn.

# Define and Deliver on Public Sector Priorities

The dozen AI use cases for climate outlined in Exhibit 3 are all important, but that doesn’t mean that they’re always equally important. Every country and region is different and each confronts its own distinct set of climate challenges given its geography, industry mix, human resources, and relative wealth. Therefore, every country or region needs to develop its own climate priorities and action plan.

For Germany, an industrial giant where the Climate Action Act mandates carbon neutrality by 2045, the priorities for AI might be accelerating the decarbonization of industries and driving energy efficiency. By contrast, Bangladesh—given its significant vulnerability to sea-level rise and extreme weather—might prioritize accelerating its National Adaptation Plan and developing early warning systems for communities.

In addition to identifying their high-priority use cases, policymakers must also expedite the application of AI to climate challenges. The public sector can serve as a pivotal catalyst for accelerating AI-supported climate action and set a compelling example for the entire economy. This is particularly important since, while 87% of organizations acknowledge the role of AI in climate action, only 40% can envision practical applications within their own operations.

# Leaders could:

- Integrate AI solutions and expertise into government strategic planning on climate priorities (for example, Nationally Determined Contributions, National Adaptation Plans, and sector-specific transition plans).

Example: AI4PublicPolicy—an initiative of the EU’s R&D program Horizon 2020—is creating an open cloud platform for automated, scalable, transparent, and citizen-centric policy management. Lisbon, for example, is using it to map its current inventory of, and expansion potential for, solar panels—with the goal of developing renewables supply forecasts to inform building codes and incentive budgets.

- Define priority sectors or use cases for AI to support climate action at local and regional levels (for example, as part of Nationally Determined Contributions, National Adaptation Plans, or National AI strategies).

# Examples:

- Denmark’s AI strategy (2019) identifies three climate-related priority areas: energy efficiency, precision agriculture, and traffic optimization.
- The Netherlands’ Strategic Plan for AI (2019) includes commitments to leverage AI in agriculture and in accelerating the energy transition.
- The UK’s AI Roadmap advocates for AI use to address climate change, particularly in the energy sector.
- The government of the Republic of the Philippines is advocating using AI to tackle climate change adaptation challenges and disaster risk reduction—in particular, through programs led by the Department of Science and Technology, such as AI for a Better Normal.

- Implement priority public sector AI solutions for climate.

# Examples:

- The US National AI Initiative Act of 2020 formalizes the National Oceanic and Atmospheric Administration’s (NOAA’s) role in coordinating AI applications for climate, ocean, Earth, and space sciences. NOAA has created the NOAA Center for Artificial Intelligence (NCAI), which collaborates across scientific fields to promote responsible and equitable AI use for environmental research.
- Singapore is using AI to predict floods and test flood-resilient infrastructure. For example, a partnership between the island nation’s National Research Foundation and the Hydroinformatics Institute (H2i) has developed Virtual Water, a surface water simulation toolbox that can predict and simulate floods resulting from heavy rainfall events.

BOSTON CONSULTING GROUP GOOGLE

# Encourage Private Sector Adoption

Policymakers could also play a catalytic role in accelerating private sector AI adoption by addressing major challenges hindering the at-scale implementation of AI for climate. Globally, we see the following five key hurdles:

To address these challenges, policymakers could activate the following five corresponding key levers:

- Create public/private partnerships to drive AI adoption in key sectors and applications
- Unclear Goals. In the absence of clear regional, national, or sector-specific objectives for climate action, AI-driven innovation may become fragmented, and resource allocation inefficient. The establishment of priority innovation domains for climate action can be a significant unlock.
- Regulatory Limitations. In some cases, particularly in heavily regulated sectors such as energy and transport, policymakers could adopt a thoughtful, risk-based governance framework for AI that ensures sufficient protections and safeguards while taking care not to stifle innovation. And, conversely, the lack of clear regulatory frameworks in other areas might also impede investment.
- Infrastructure Challenges. Many high-emission sectors rely on legacy infrastructure that cannot readily support AI technologies. For example, outdated road networks may struggle to accommodate smart traffic management systems powered by AI—or limited penetration of smart meters could hinder the at-scale deployment of AI-based energy efficiency solutions.
- Innovation Costs. Developing and implementing AI solutions often demands significant financial resources and time. Giving access to specific innovation platforms, such as high-performing computing infrastructure—or to targeted innovation funding—can remove significant barriers to innovation for the innovation ecosystem broadly, and particularly for small and medium-sized enterprises.
- Deployment Costs. In many areas, there may be significant entry or adoption costs, including capacity and capability needs, that pose challenges for companies, their stakeholders, and customers. For example, the adoption and implementation at scale of precision agriculture could be held back because of farmer concerns regarding the expense of installing the Internet of Things hardware needed to support it.

- Remove regulatory barriers to and provide regulatory support and clarity for AI adoption
- Accelerate infrastructure modernization and digitalization to enable AI use
- Support AI research and innovation in climate-relevant domains by involving both academia and the private sector
- Optimize incentives to drive AI adoption at scale for climate action priorities when existing mechanisms are insufficient (for example, public funding, tax credits, etc.)

Nonetheless, these levers need to be tailored to the distinct challenges of each jurisdiction and sector. These challenges are shaped by both global and context-dependent factors such as market intricacies, complexity, regulatory frameworks, and innovation dynamics. Therefore, policymakers could adopt a strategic approach by identifying the most effective measures to address these challenges and determining the appropriate level of intervention, whether through advocacy, incentives, or binding measures. They could also draw insights from best practices within each sector and jurisdiction, as well as across sectors and jurisdictions, in order to learn from one another.

For example, consider the implementation of AI in grid planning and management. AI solution developers may encounter a constraint that necessitates holding specific licenses to test or develop their solutions. In such circumstances, policymakers might consider issuing regulatory waivers or establishing controlled testing environments. Similarly, in regions with limited smart meter adoption, policymakers could take action by allocating funding for infrastructure modernization or offering incentives to encourage electricity providers to replace aging meters. These measures would facilitate the integration of AI applications designed to improve the energy efficiency of buildings.

To underscore sectoral distinctions, in the following, we provide examples to illustrate how policymakers have begun implementing policies in sector-specific contexts.

35 ACCELERATING CLIMATE ACTION WITH AI

# Leaders could:

Create public/private partnerships to drive AI adoption within and across key sectors and applications.

# Examples:

- Buildings: DO IT SMARTer—a public-private partnership between the Technical University of Cluj-Napoca, Øsfold University College, the Norwegian company NxTech, Romania’s Alba Iulia municipality, and the NGO Center for the Study of Democracy—seeks to develop AI-driven energy efficiency solutions for public buildings in Romania and Norway.
- Energy: The US Department of Energy’s Princeton Plasma Physics Laboratory is partnering with the Renaissance Fusion startup on AI-driven efforts to accelerate the development of carbon-free fusion energy.
- Transport: In Project Green Light, Google is collaborating with 12 cities including Manchester, Rio de Janeiro, Jakarta, and Abu Dhabi to reduce stop-and-start events through AI-supported traffic light management. Early indicators show a potential for up to a 30% reduction in stops, which could reduce emissions at intersections up to 10%. This could have a significant impact, as cars at city intersections generate 29 times more pollution than do cars on the open road.

Remove regulatory barriers to and provide regulatory support and clarity for AI adoption.

# Examples:

- Electricity: Spain, Brazil, and Australia have launched regulatory “sandboxes” for their electricity sectors that can offer waivers for climate-related pilots. In Australia, for example, grid participants can be granted exemptions from registering as a network service provider.
- Agriculture: Key agro-food stakeholders have co-signed a set of non-binding guidelines entitled the EU Code of Conduct on Agricultural Data Sharing. Similarly, The American Farm Bureau Federation has worked with stakeholders to establish the Privacy and Security Principles for Farm Data.

Accelerate infrastructure modernization and digitalization to enable AI use.

# Examples:

- Buildings: In 2022, the UK government imposed new binding requirements that energy suppliers install smart meters in homes and small businesses. The target, currently under negotiation, aims for 80% smart meter coverage in homes and 73% in small businesses by 2025.
- Energy: The Modernization Fund is a dedicated funding program to support 10 lower-income EU Member States in modernizing their energy systems and improving energy efficiency (for example, modernization of energy networks, district heating, etc.). Similarly, adopted in late 2022, the Digitalizing the energy sector – EU action plan, which is characterized by cybersecurity, efficiency, and sustainability, aims to cultivate a competitive marketplace for digital energy services and digital energy infrastructure.

Support AI research and innovation in climate-relevant domains by involving both academia and the private sector.

# Examples:

- Energy: In May 2023, the US Department of Energy announced a $40 million investment in 15 projects focused on developing high-performance, energy-efficient cooling solutions for data centers.
- Agriculture: The EU’s Horizon 2020 program for research and innovation has allocated more than €200 million to support the deployment of precision farming.

BOSTON CONSULTING GROUP GOOGLE 36

# Industry: The UK’s Project Bluebird

is creating a digital twin of UK airspace that, by identifying ways to make air traffic control more efficient, can help the aviation industry achieve its goal of net zero by 2050.

# Urban planning: Virtual Singapore

a collaboration between the National Research Foundation, the Land Authority, and the Government Technology Agency—uses topographic and dynamic data to create a 3D digital replica of the nation state that is the official platform for simulation and virtual testing of urban planning solutions.

# Optimize incentives to drive AI adoption at scale for climate action priorities when existing mechanisms are insufficient (for example, public funding, tax credits, etc.).

# Examples:

# Agriculture:

Australia has launched the Farms of the Future AgTech Grant Program to encourage farmers to adopt precision agriculture to boost productivity and improve resource management, including water efficiency and drought readiness.

# Buildings:

The US Federal-State Buy Clean Partnership is a commitment by the federal government and 13 states to purchase lower-carbon materials for federal and state-funded projects with the goal of reducing emissions and sending a unified demand signal to the market.

# Industry:

Singapore’s Energy Efficiency Fund offers five different grant programs that reimburse businesses up to 70% of investments that improve the energy efficiency of industrial facilities. Similarly, Japan’s Ministry of Economy, Trade, and Industry is offering subsidies to promote the adoption of energy-efficient technologies in the industrial and commercial sectors.

# Guide AI for Climate

Policymakers play a crucial role in shaping the evolution of AI—not just in accelerating its positive contributions, but also in minimizing its potential negative impacts. With regard to AI for climate, clear principles and guidelines are essential in two areas: first, maximizing the environmental friendliness of AI applications, and second, ensuring that AI applications respect the privacy and diversity of people and do not inadvertently exacerbate inequalities. We discuss each in turn.

# Address Environmental Impacts of AI Operations

As discussed in the previous chapter, AI has its own environmental footprint. And while it has not yet been comprehensively measured, it is essential that we monitor and manage it.

AI developers recognize the necessity of minimizing AI’s environmental footprint, especially in the context of expanding the use of AI—and are already working to make algorithms and data centers more energy efficient and to increase their commitment to renewables. For instance, in terms of clean energy utilization, several organizations such as the Clean Energy Buyers Association (CEBA) in the US, RE-Source in the EU, and the Asia Clean Energy Coalition (ACEC) in APAC (each with members including prominent tech players) are actively advocating for the acceleration and facilitation of access to carbon-free energy for corporate buyers in various regions.

37 ACCELERATING CLIMATE ACTION WITH AI

# Leaders could:

Promote transparency of AI’s environmental impact and potential via pragmatic reporting guidelines and standards.

# Examples:

The European Code of Conduct for Data Centres is an initiative led by the European Joint Research Centre. Since 2020, this initiative has regularly released annual guidelines and ambitious voluntary standards aimed at promoting energy efficiency best practices within data centers. These guidelines encompass recommendations pertaining to energy consumption, as well as environmental measurement and reporting.

Spain’s National Green Algorithms Plan seeks to raise awareness among AI developers of the energy consequences of their design decisions—and to draw attention to more sustainable choices through the development of standards and tools to measure the energy consumption of algorithms.

The German Bundestag has amended its Energy Efficiency Act, which includes specific regulations for data centers and provisions concerning the incorporation of renewable energy sources into data center energy portfolios, standards for Power Usage Effectiveness (PUE), and mandates for the reuse of heat generated by data centers.

# Encourage AI technology providers to make robust sustainability and clean energy commitments—and to adopt climate-friendly development best practices.

# Examples:

The 24/7 Carbon-Free Energy Compact was introduced during the High-level Dialogue on Energy in 2021. The participants in the Compact—both Member States and non-state entities—committed to a set of principles that will lead to energy policies, technologies, procurement practices, and solutions that transform the broader energy ecosystem with the goal of achieving a carbon-free energy grid.

The Climate Neutral Data Center Pact is a self-regulatory initiative that includes 100+ data center operators and trade associations to make data centers in Europe climate neutral by 2030.

# Facilitate the adoption of sustainable practices for AI operations by supporting investment to reduce AI’s environmental impact and removing barriers to clean technology adoption (for example, reforming planning for energy infrastructure, market rules, etc.).

# Examples of access to clean energy:

The European Commission is working to establish an ambitious target to increase the renewables share of its energy mix to more than 40% by 2030, while in the US, the Biden administration has set an ambitious goal to achieve a 100% carbon-free electricity sector by 2035. These overarching frameworks instill confidence among investors, fostering the growth of clean energy industries.

Governments across Europe (including the UK, Norway, and Estonia) and elsewhere (such as South Africa, Brazil, and India) employ competitive auctions for sourcing clean energy—an approach that offers distinct advantages over more traditional fixed-price subsidies (for example, feed-in tariffs).

# Examples of access to clean tech:

The US Inflation Reduction Act of 2022 offers tax incentives and other financial rewards for purchasing equipment that reduces and/or sequesters carbon.

The EU’s Green Deal Industrial Plan of 2023, among other initiatives, provides funding to accelerate the growth of Europe’s clean tech industry.

BOSTON CONSULTING GROUP GOOGLE

# Promote the Socially Responsible Use of AI for Climate

As discussed in the previous chapter, AI introduces several social risks that require mindful management to ensure the benefits of AI for climate are broadly shared.

For example, one significant concern is bias within AI models, where skewed or limited training data can lead to biased outcomes. For instance, if climate-related algorithms do not consider the specific context and needs of the communities most affected, biased model output will hold back progress. Additionally, there are regional disparities. The Global South faces more climate challenges, while AI expertise and infrastructure remain predominantly concentrated in the Global North. This disparity can limit access to AI-driven solutions where they are needed most. Moreover, AI’s potential for misinformation poses a threat to informed climate discourse, as the technology can be exploited to influence public perception. Lastly, data privacy and security must be a priority, as AI applications entail the handling of sensitive information, and breaches could have severe consequences.

# Leaders could:

Engage widely with all stakeholders to develop and communicate principles for socially responsible AI, addressing such factors as fairness, inclusiveness, safety, and data privacy.

# Examples:

UNESCO’s Recommendation on the Ethics of AI features 10 principles that define a human-rights-centered approach to AI development, including do-no-harm, data protection, human oversight, and non-discrimination. Similarly, the OECD AI Principles, adopted in 2019, define five key principles for an AI that is innovative and trustworthy and respects human rights and democratic values. In the US, the Blueprint for an AI Bill of Rights identifies five principles that should guide the design, use, and deployment of automated systems, as well as a handbook to move from principle to practice. The European High-Level Expert Group on AI has developed Ethics Guidelines for Trustworthy Artificial Intelligence.

# Create assessment frameworks

to measure the alignment of AI applications with socially responsible principles.

# Example:

The AI Verify Foundation, an initiative of Singapore’s Infocomm Media Development Authority, offers a framework and tools to assess AI applications along key ethical dimensions such as safety, security, and fairness.

39

ACCELERATING CLIMATE ACTION WITH AI

Keeping warming to below the Paris Agreement’s 1.5°C target will require bold and responsible action on the part of policymakers, business leaders, and technologists.

It may also require them to take different, more agile, collaborative, and transparent approaches. Agile because of the evolving impacts of climate change and the rapid pace of progress in AI and climate science; and collaborative and transparent because no single stakeholder necessarily has access to all the data and expertise needed to address its climate challenges—and insights often bloom when different perspectives come together.

As we argue in this report, even at the current state of the technology, AI has the potential to make a significant net positive contribution to addressing the climate challenge—and there are already many inspiring lighthouse examples of its application. However, time is of the essence!

BOSTON CONSULTING GROUP GOOGLE 40

# Endnotes

# Executive Summary

1 Scope 1 emissions refer to direct emissions from sources the organization owns or controls (for example, its own vehicles and production equipment). Scope 2 comprises indirect emissions from purchased energy (for example, electricity). Scope 3 includes indirect emissions across the value chain, whether from suppliers (excluding purchased energy) or product usage by customers.

# The Climate Action Imperative and the Promise of AI

2 Emissions Gap Report 2022, UNEP, 2022.

3 Groundswell: Preparing for Internal Climate Migration, The World Bank, 2018.

4 NDC Synthesis Report, UNFCCC (UN Climate Change), 2022.

5 The IPCC Working Group III report, Climate Change 2022: Mitigation of climate change, estimates that for the world to achieve net zero by 2050, emissions would need to be reduced by 43% by 2030.

6 How AI can enable a sustainable future, PwC/Microsoft, 2019.

7 How artificial intelligence can power your climate action strategy, Capgemini, 2020.

# How AI Can Help Accelerate Climate Action

8 We include avoided emissions in our analyses. For example, how—by identifying new transition pathways for developing countries—they can grow their economies with fewer emissions, thereby “avoiding” emissions that would have been generated had they simply pursued a “business as usual” approach to growth.

9 Machine learning can boost the value of wind energy, Google Blog, February 2019.

10 New ways we’re helping reduce transportation and energy emissions, Google Blog, October 2023.

11 Google Environmental Report 2023, p. 6.

12 Ibid., p. 28.

13 How AI is helping airlines mitigate the climate impact of contrails, Google Blog, August 2023.

14 Rogelj, J. et al., Mitigation Pathways Compatible with 1.5°C in the Context of Sustainable Development, in Global Warming of 1.5°C. An IPCC Special Report on the impacts of global warming of 1.5°C above pre-industrial levels and related global GHG emission pathways, in the context of strengthening the global response to the threat of climate change, sustainable development, and efforts to eradicate poverty, 2018.

15 TCFD Insights Series | S&P 500, Carbon Disclosure Project, September 2022. Carbon Disclosure Project (CDP), a nonprofit charitable organization, operates a worldwide disclosure platform that empowers investors, corporations, municipalities, and governmental regions to effectively oversee their ecological footprints.

16 Zvika Ben-Haim and Omer Nevo, Real-time tracking of wildfire boundaries using satellite imagery, Google Research, 2023.

17 How AI is improving agriculture sustainability in India, Google Blog, January 2023.

18 New ways we’re helping reduce transportation and energy emissions, Google Blog, October 2023.

19 Ibid., Google Blog, October 2023.

20 How we’re using AI to combat floods, wildfires and extreme heat, Google Blog, October 2023.

# Navigating AI's Potential Risks

21 IEA analysis (accessed in September 2023) based on Masanet et al. (2020), Malmodin (2020), Hintemann & Hinterholzer (2022) and reported energy use data from large data center operators.

22 Kaack, L.H. et al., Aligning artificial intelligence with climate change mitigation, Nature Climate Change, 12, 518–527, 2022.

23 Masanet, E. et al., Recalibrating global data center energy-use estimates, Science, 2020.

24 Google Environmental Report 2023, p. 38.

25 Patterson, D. et al., The Carbon Footprint of Machine Learning Training Will Plateau, then Shrink, 2022.

26 Electric Grid Carbon intensity based on Ember’s Yearly Electricity Data; Ember’s European Electricity Review; Energy Institute Statistical Review of World Energy, 2022.

27 Based on IEA publication, Renewable energy section, accessed in September 2022.

# AI for Climate: A Summary of Critical Policy Outcomes

A data catalog functions as a comprehensive data inventory. It maintains a record of all accessible data, helping users swiftly locate specific information.

# References

1. Google Deepmind Blogpost, Machine learning can boost the value of wind energy, February 2019.
2. Patterson, D. et al., Carbon Emissions and Large Neural Network Training, 2021.
3. Patterson, D. et al., The Carbon Footprint of Machine Learning Training Will Plateau, then Shrink, 2022.
4. The computing power needed to train AI is now rising seven times faster than ever before; MIT Technology Review, 2019; What Is a Transformer Model? NVIDIA, 2022.
5. So, David R. et al., Primer: Searching for Efficient Transformers for Language Modeling, 2021.
6. IBM Global Adoption Index, 2022.
7. NVIDIA estimates that 80-90% of the AI/ML workload is for inference. Amazon Web Services estimates that 90% of AI/ML demand in the cloud is for inference.
8. Google Environmental Report 2023. p.50.
9. Siddik, M. et al., The environmental footprint of data centers in the United States, Environmental Research Letters, 16 064017, 2021.
10. Total annual data centers water consumption estimated to 626 billion liters, of which 95–100 billion liters used on-site for cooling; Shehabi, Arman, Smith, Sarah, Sartor, Dale, Brown, Richard, Herrlin, Magnus, Koomey, Jonathan, Masanet, Eric, Horner, Nathaniel, Azevedo, Inês, & Lintner, William. United States Data Center Energy Usage Report. United States. Figure 25.
11. Our commitment to climate conscious data center cooling. Google Blog. November, 2022.
12. Google Environmental Report 2023, p. 95.
13. Based on USGS estimations of water use in the United States in 2015: USA Environmental Protection Agency, Water sense, statistics and facts. Based on an average household size of 2.5 persons with each American using an average of 82 gallons of water a day at home.
14. Meta, Public Water Reporting: Expanding the Operating Envelope.
15. Azure Microsoft, Learn how Microsoft Circular Centers are scaling cloud supply chain sustainability, 2022.
16. Google Environmental Report 2023, p. 57.
17. Google AI Principles.
18. Accra.
19. The Affordability of ICT Services 2022, ITU Policy Brief, 2022.
20. Artificial Intelligence needs assessment survey in Africa, UNESCO, 2021.
21. Strengthening AI Governance: UNESCO Pilots its Capacity Building Framework on Digital Transformation in Africa and India, UNESCO News, July 2023.
22. Seow, P. et al., Educational Policy and Implementation of Computational Thinking and Programming: Case Study of Singapore, a chapter in Computational Thinking Education, Kong, SC. and Abelson, H., editors, Springer, Singapore.
23. Decarbonization: A Win-Win for the Economy and Ecology, Germany Works.
24. Digital Decarbonization Germany, Accelerating Germany’s climate protection with efficient digital solutions, Implement Consulting study commissioned by Google, 2023.
25. Gailhofer, P. et al., The role of Artificial Intelligence in the European Green Deal, a study for the special committee on Artificial Intelligence in a Digital Age (AIDA), Policy Department for Economic, Scientific and Quality of Life Policies, European Parliament, Luxembourg, 2021.
26. “Concentration dynamics of coarse and fine particulate matter at and around signalised traffic intersections,” Environmental Science: Processes & Impacts, 2016.

# About the Authors

# BCG

Hamid Maher is a managing director and partner in BCG’s Casablanca office. He heads BCG X in Africa and is a founding and steering committee member of the AI for the Planet Alliance—and leads BCG’s engagement as the alliance’s knowledge partner. He can be reached at maher.hamid@bcg.com.

Amane Dannouni is a managing director and partner in BCG’s Casablanca office and leads the firm’s digital and technology practice in Africa. One of his areas of focus is the nexus between technology and sustainable development at the company, country, and regional levels. He can be reached at dannouni.amane@bcg.com.

Edmond Rhys Jones is a partner and associate director in BCG’s London office. He co-leads BCG’s Center for Climate and Sustainability Policy and Regulation and is a core member of the Climate and Sustainability practice. He can be reached at rhysjones.edmond@bcg.com.

Stefan A. Deutscher is a partner and director in BCG’s Berlin office. He is a core member of BCG’s Technology Advantage and Technology, Media & Telecommunications practices. He is BCG’s global topic leader for IT infrastructure and data center operation. He can be reached at deutscher.stefan@bcg.com.

Hamza Tber is an associate director in BCG’s Casablanca office. Prior to joining BCG, he was senior program officer, United Nations, Executive Office of the Secretary General, Climate Action team. He can be reached at tber.hamza@bcg.com.

Ali Ziat is a principal specializing in data science based in BCG’s Casablanca office. He holds a Ph.D. in AI and Machine Learning and has been involved in the development of several climate-related AI tools. He can be reached at ziat.ali@bcg.com.

Amjad Kharij is a project leader in BCG’s Casablanca office. He can be reached at kharij.amjad@bcg.com.

Ghita Dezzaz is an associate in BCG’s Casablanca office. She can be reached at dezzaz.ghita@bcg.com.

# Google

Adam Elman is the head of Sustainability for Google Europe, Middle East, and Africa, and leads the company’s sustainability work across the region.

Marsden Hanna is the head of Sustainability and Climate Policy at Google, where he leads the company’s engagement with governments on sustainability, climate, and energy policy issues.

David Patterson is a distinguished software engineer at Google, working on domain-specific computer architectures for machine learning.

Maud Texier is the global director of Clean Energy and Decarbonization Development at Google. She leads a team responsible for developing and scaling 24/7 carbon-free energy for Google’s global infrastructure worldwide.

Juliet Rothenberg is the group product manager of Climate AI at Google Research, leading product management for Climate AI initiatives within Google Research.

Antonia Gawel is the global director of Sustainability and Partnerships at Google, responsible for furthering Google’s global climate and sustainability goals through partnership.

# For Further Contact

If you would like to discuss this report, please contact the authors.

BOSTON CONSULTING GROUP GOOGLE 44

# Acknowledgements

The authors would like to express their gratitude to the many leading topic experts on AI, climate, technology, data centers, and policy who graciously shared their time and perspectives with us. Without their contributions, this report would not have been possible. You can find the full list of interviewees below.

|Interviewee|Company|Title|
|---|---|---|
|Jacques Amselem|Albo Climate|CEO and Co-Founder|
|Jen Bennett|Google|Technical Director, Sustainability, Office of the CTO|
|Kate Brandt|Google|Chief Sustainability Officer|
|William Brent|Husk Power Systems|Chief Marketing Officer|
|Helen Elizabeth Burdett|World Economic Forum|Head of Technology for Earth|
|Mark Caine|Google|Senior Lead, Energy & Climate|
|François Candelon|BCG|Global Director, BCG Henderson Institute|
|Charlotte Degot|CO2 AI|CEO & Founder|
|Val Elbert|BCG|Managing Director and Partner, Telecom & Media Growth Strategy, Digital Transformation|
|Charlotte Gastineau|BCG|Associate|
|Sarah Goodman|BCG|Partner and Associate Director, Public Sector|
|Alon Harris|Google|Program Manager, Research & Search|
|Gemma Jennings|Google DeepMind|Product Manager|
|Vilma Kaza|Google|EU Sustainability and Climate Policy Lead|
|Justin Keeble|Google|Managing Director for Global Sustainability|
|Ashley King-Bischof|Sprout|Founder, CEO, CPTO|
|Shivam Kishore|UN Environment Program|Senior Advisor, Digital Transformation, Sustainability|
|Naomie Lecard|Albo Climate|Head of Business Development|
|Brian (Juhyuk) Lee|Google.org|Sustainability team|
|Ronit Levavi Morad|Google|Director, Program Management, Research & Search|

# Interviewee

|Interviewee|Company|Title|
|---|---|---|
|Mathieu Marcotte|CEIMIA|Director, AI Ecosystem Mobilization and Special Projects|
|Travis McCoy|Google|Director, Product Management, Climate & Sustainability|
|Nicolas Miailhe|The Future Society|Founder and President|
|Steven Mills|BCG|Chief AI Ethics Officer, Lead for AI in Public Sector|
|Reina Otsuka|UN Development Program|Digital Innovation Lead for Nature, Climate, and Energy|
|John Platt|Google|Distinguished Scientist|
|Golestan (Sally) Radwan|UN Environment Program|Chief Digital Officer|
|Kirsten Rulf|BCG|Partner and Associate Director, Data & Digitalization|
|Leonor Saitkoulov|BCG|Senior Data Scientist|
|Duncan Smith|Google DeepMind|External Comms Senior Manager|
|Ben Townsend|Google|Global Head of Data Center Sustainability|
|Joseph Wegener|World Economic Forum|Project Fellow|
|Mike Werner|Google|Global Head of Circular Economy|
|Sims Witherspoon|Google DeepMind|Climate Action Lead|
|David Young|BCG|Managing Director & Senior Partner, Global Topic Leader for Total Societal Impact/Sustainability|
|Ashley (Schoettle) Zlatinov|Google|AI Policy Lead, Social Impact|

BOSTON CONSULTING GROUP       GOOGLE                                                                         46

# References

# General resources on AI and its potential for climate action

- Digital Decarbonisation: How the digital sector is supporting climate action
- Climate AI: How artificial intelligence can power your climate action strategy
- The role of Artificial Intelligence in the European Green Deal
- Environmental and ethical considerations
- Measuring the environmental impacts of artificial intelligence compute and applications: The AI footprint
- Sustainable AI: Environmental Implications, Challenges, and Opportunities
- The Presidio Recommendations on Responsible Generative AI
- Recommendation on the Ethics of Artificial Intelligence
- A Policy Roadmap for 24/7 Carbon-Free Energy
- AI for climate in the context of policymaking
- Climate Change and AI: Recommendations for Government Action

# ITI’s Global AI Policy Recommendations

- Biodiversity and Artificial Intelligence: Opportunities & Recommendations for Action
- Final report on bridging data gaps
- Data adaptation at different and temporal scales
- AI Excellence: Enabling conditions for AI’s development and uptake
- Artificial Intelligence in the Public Sector
- Beijing Consensus on Artificial Intelligence and Education
- Artificial Intelligence and Digital Transformation: Competencies for Civil Servants
- Stakeholders for a Cohesive and Sustainable World: The Role of Lighthouse Projects
- Artificial Intelligence and International Affairs: Disruption Anticipated

# Sponsor(s)

- A Google-commissioned report from Implement Consulting Group, 2022
- A report from Capgemini, 2020
- A report from the European Parliament’s special committee on Artificial Intelligence in a Digital Age, May 2021
- A report from the OECD in collaboration with The Global Partnership on Artificial Intelligence, 2022
- An academic article, Facebook AI, 2022
- A report from the World Economic Forum in collaboration with AI Commons, 2023
- A report from UNESCO, 2021
- A report from Google, 2022
- A report from the Global Partnership on AI in collaboration with Climate Change AI and the Centre for AI & Climate, November 2021
- A report from the Information Technology Industry Council, 2021
- A report from The Global Partnership on Artificial Intelligence, 2022
- A technical document from the Network for Greening the Financial System, 2022
- A technical paper from the Adaptation Committee of the United Nations Framework Convention on Climate Change, the Kyoto Protocol, and the Paris Agreement, 2020
- A report from the European Commission, laying out the EU’s coordinated plan on artificial intelligence, 2021
- A report from the GovTech Global Partnership in collaboration with the World Bank, 2020
- A report from UNESCO, 2019
- A report from UNESCO, November 2022
- A briefing paper from the World Economic Forum, January 2020
- A report from Chatham House, 2018

# Add Co-Sponsor logo here

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

Uciam volora ditatur? Axim voloreribus moluptati autet hario qui a nust faciis reperro vitatia dipsandelia sit laborum, quassitio. Itas volutem es nulles ut faccus perchiliati doluptatur. Estiunt. Et eium inum et dolum et et eos ex eum harchic teceserrum natem in ra nis quia disimi, omnia veror molorer ionsed quia ese veliquiatius sundae poreium et et illesci atibeatur aut que consequia autas sum fugit qui aut excepudit, omnia voloratur? Explige ndeliaectur magnam, que expedignist ex et voluptaquam, offici bernam atqui dem vel ius nus.

Nem faccaborest hillamendia doluptae conseruptate inim volesequid molum quam, consequa consedipit hillabo. Imaio evelenditium haribus, con reictur autemost, vendam am ellania estrundem corepuda derrore mporrumquat.

For information or permission to reprint, please contact BCG at permissions@bcg.com.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com.

Follow Boston Consulting Group on Facebook and X (formerly known as Twitter).

© Boston Consulting Group 2023. All rights reserved.

11/23

                        Ei
                2
         &
                            4
        &                         0
   @ 0 4                     8 @Pe2
                                  3
#| 1#, 3e0 &  % 4 90Ea
  EG                        Google