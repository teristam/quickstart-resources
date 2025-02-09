PERSPECTIVE
published: 13 December 2019
doi: 10.3389/fphar.2019.01488

Striatal Cholinergic Interneurons:
How to Elucidate Their Function in
Health and Disease

Nicolas Mallet 1,2, Arthur Leblois 1,2, Nicolas Maurice 3 and Corinne Beurrier 3*

1 Université de Bordeaux, Institut des Maladies Neurodégénératives, Bordeaux, France, 2 CNRS UMR 5293, Institut des
Maladies Neurodégénératives, Bordeaux, France, 3 Aix Marseille Univ, CNRS, IBDM, Marseille, France

Striatal cholinergic interneurons (CINs) are the main source of acetylcholine in the striatum
and are believed to play an important role in basal ganglia physiology and
pathophysiology. The role of CINs in striatal function is known mostly from extracellular
recordings of tonically active striatal neurons in monkeys, which are believed to
correspond to CINs. Because these neurons transiently respond to motivationally cues
with brief pauses, ﬂanked by bursts of increased activity, they are classically viewed as key
players in reward-related learning. However, CIN modulatory function within the striatal
network has been mainly inferred from the action of acetylcholine agonists/antagonists or
through CIN activation. These manipulations are far from recapitulating CIN activity in
response to behaviorally-relevant stimuli. New technical tools such as optogenetics allow
researchers to speciﬁcally manipulate this sparse neuronal population and to mimic their
typical pause response. For example, it is now possible to investigate how short inhibition
of CIN activity shapes striatal properties. Here, we review the most recent literature and
show how these new techniques have brought considerable insights into the functional
interesting and novel
role of CINs in normal and pathological states, raising several
questions. To continue moving forward, it is crucial to determine in detail CIN activity
changes during behavior, particularly in rodents. We will also discuss how computational
approaches combined with optogenetics will contribute to further our understanding of
the CIN role in striatal circuits.

Keywords: striatal cholinergic interneurons, basal ganglia, optogenetics, computational modelling,
Parkinson’s disease

INTRODUCTION

Edited by:

Véronique Sgambato,
Institut National de la Santé et de la
Recherche Médicale (INSERM),
France

Reviewed by:

Jill Crittenden,
Massachusetts Institute of
Technology, United States
John N. J. Reynolds,
University of Otago, New Zealand

*Correspondence:

Corinne Beurrier
corinne.beurrier@univ-amu.fr

Specialty section:

This article was submitted to
Neuropharmacology,
a section of the journal
Frontiers in Pharmacology

Received: 10 September 2019
Accepted: 15 November 2019
Published: 13 December 2019

Citation:

Mallet N, Leblois A, Maurice N and
Beurrier C (2019) Striatal Cholinergic
Interneurons: How to Elucidate Their
Function in Health and Disease.
Front. Pharmacol. 10:1488.
doi: 10.3389/fphar.2019.01488

The striatum is a brain region containing high levels of acetylcholine (ACh), muscarinic receptors,
and other ACh-related markers (Weiner et al., 1990; Hersch et al., 1994). Cholinergic interneurons
(CINs) are the main source of ACh in the striatum [but see (Dautan, 2014)]. Despite their small
numbers (1–3% of all striatal cells) and scattered distribution throughout the striatum, CINs have
dense terminal ﬁelds that overlap those of dopaminergic projections coming from the substantia

Frontiers in Pharmacology | www.frontiersin.org

1

December 2019 | Volume 10 | Article 1488

Mallet et al.

Investigating CIN Functional Role

nigra pars compacta (Bolam et al., 1984). CINs contact the two
populations of striatal output neurons (also called medium spiny
neurons, MSNs) that express either the dopamine D1 or D2
receptors. While most striatal neurons are not autonomously
active, CINs exhibit a regular spiking activity in absence of any
synaptic inputs (Bennett et al., 2000). Extracellular recordings
performed in vivo in the striatum of monkeys also reveal the
presence of tonically active neurons (TANs), which are thought
to correspond to CINs (Aosaki et al., 1995). Hence, the
morphofunctional features of CINs—mainly their extensive
arborization primarily directed to MSNs and their tonic
activity—place them as potent modulators of striatal output.
Striatal output regulation is a fundamental process of the basal
ganglia functioning, as a balanced activity between D1 and
D2 MSNs is required to ensure correct motor and
cognitive behaviors.

The improvement of parkinsonian tremor by both
dopaminergic agonists and anticholinergic drugs led to the
dopamine (DA)-ACh balance hypothesis, where DA and ACh
are believed to play opposite roles in the striatum (Barbeau,
1962). Even though the prescription of anticholinergic drugs has
been phased out due to their side-effects, this long standing
clinical observation underlines the functional impact of ACh as
the level of DA falls and has often led to the consideration of
Parkinson’s disease (PD) as a hypercholinergic disorder [but see
(McKinley, 2019)]. There is indeed compelling evidence showing
that DA depletion triggers complex alterations in striatal
cholinergic signaling, activity, and connectivity (Aosaki, 1994;
Raz, 2001; Ding, 2006; Salin, 2009). However, there is no
consensual view explaining how CINs contribute to motor
symptoms and abnormal network dynamic in PD.

At the cellular level, CIN modulation of the striatal network
has been mainly inferred from the action of ACh agonists or
through CIN activation. While nicotinic receptors (nAChRs) are
expressed by interneurons and extrinsic afferent terminals,
MSNs respond to ACh exclusively via muscarinic receptors
(mAChRs): M1 receptors are present on D1 and D2 MSNs
and M4 receptors are preferentially expressed by D1 MSNs.
Activation of mAChRs modulates an array of voltage-gated
channels and intracellular pathways in MSNs. Determining the
combinatorial effect of these actions, potentially even opposing
each other, is highly challenging and has recently been covered at
length by excellent recent reviews (Tanimura, 2018; Ztaou and
Amalric, 2019; Abudukeyoumu et al., 2019). A hallmark of CINs
is their continuous tonic activity, which is expected to lead to a
high level of ACh in the striatum, and the stereotypical bursts
and pauses activity that they acquire during sensorimotor
learning (Apicella, 2007). We can assume that a drop in ACh
release, as expected to happen after a brief decrease in ﬁring,
conveys meaningful information to the striatal network. A recent
hypothesis proposes that the pause would open a permissive
temporal window during which corticostriatal synaptic plasticity
occurs (Deffains and Bergman, 2015). However, it is still unclear
how inhibition of CIN activity shapes striatal properties. Here,
we review the related literature and show how optogenetic and

computational approaches may contribute to further our
understanding of this topic.

CONSEQUENCES OF CHOLINERGIC
INTERNEURON INHIBITION ON STRIATAL
PROPERTIES

The widespread excitatory input from the cortex targeting D1
and D2 MSNs sets the activity of the direct and indirect
striatofugal pathways which play a fundamental role in
movement planning and action selection. Understanding how
CINs modulate the dynamics of corticostriatal processing and
MSN activity is therefore essential to uncover basal ganglia
function. Cholinergic modulation of long-term corticostriatal
plasticity has been addressed in excellent reviews (Lovinger, 2010;
Lerner and Kreitzer, 2011) and will not be further discussed here.
The effects of cholinergic antagonists on corticostriatal
transmission might provide interesting insights to predict how
a pause in CIN ﬁring impacts striatal output. It was reported that
atropine, a broad mAChRs antagonist, or methoctramine, at a
concentration that blocks M2 and M3 mAChRs, lead to a modest
increase in corticostriatal transmission via the inhibition of
mAChRs located on the glutamatergic terminals, suggesting
the existence of tonic cholinergic presynaptic inhibition
(Pakhotin and Bracci, 2007). On the other hand, pirenzepine, a
blocker of M1 mAChRs, reduces corticostriatal transmission
(Wang, 2006; Tozzi, 2011). In these last two studies, the
authors suggest that lowering M1 mAChR activity in MSNs
leads to the opening of L-type Ca2+ channels, which then triggers
endocannabinoids release. Endocannabinoids are then able to
reduce glutamate transmission by activating presynaptic CB1
receptors. Hence, mAChRs inhibition could exert opposite
actions on basal corticostriatal transmission depending on
their pre- or postsynaptic localization. Nicotinic a7 receptors
have been described on cortical glutamatergic terminals but
whether these receptors directly modulate corticostriatal
transmission is still unclear (Howe et al., 2016).

One of the caveats of pharmacological experiments is that
they do not allow to assess the effects of endogenous ACh that
depends on the temporal dynamic of CIN ﬁring. Moreover, CINs
might co-release glutamate and GABA along with ACh, with
effects that cannot be apprehended through this approach
(Higley et al., 2009; Lozovaya, 2018). Optogenetic
manipulations, enabling control of electrical activity in speciﬁc
cell types with high temporal accuracy, can provide substantial
insights into these issues. Here, we review the few studies
showing the impact of optogenetic inhibition of CIN activity in
the dorsal striatum. In vitro, we and others have shown that
inhibition of CIN ﬁring with halorhodopsin (eNpHR) is
associated with a decrease in D1 and D2 MSN excitability that
might involve a lowering of M1 mAChRs activation (Maurice,
2015; Zucca et al., 2018). In anaesthetized mice, opto-inhibition
of eNpHR-expressing CINs was also reported to decrease MSN
activity by hyperpolarizing their membrane potential and

Frontiers in Pharmacology | www.frontiersin.org

2

December 2019 | Volume 10 | Article 1488

Mallet et al.

Investigating CIN Functional Role

increasing the duration of down states (Zucca et al., 2018). In
contrast, eNpHR-induced inhibition of CIN ﬁring in freely
moving mice did not alter MSN activity (English, 2011). In
this last study, it is the rebound of action potentials occurring at
the end of the eNpHR-induced hyperpolarization that triggered a
decrease in MSN ﬁring. Interestingly, despite the cellular effect
induced by this pause-rebound, it was not followed by any
detectable behavioral responses (English, 2011). This is in
agreement with other works showing that opto-inhibition of
CIN ﬁring does not affect locomotion, anxiety‐like behavior,
social memory recognition, and visuospatial object recognition
(Maurice, 2015; Ztaou et al., 2018). In contrast, the behavior of
PD mice, which perform poorly in all these tests, is improved by
CIN silencing (Maurice, 2015). Restoring the balance between
the striatofugal pathways at the level of the substantia nigra pars
reticulata might be one component of the positive effect of CIN
inhibition in parkinsonian condition (Maurice, 2015).

What conclusions can we draw from this brief overview?
Obviously, more work is needed to understand how CIN
inhibition shapes striatal output and modulates basal ganglia-
related behavior. The conﬂicting effects of CIN ﬁring inhibition
on MSN activity and the lack of clear behavioral response in
normal mice can be interpreted in different ways: (i) the light
parameters (i.e. light duration, pattern or timing delivery) used
to manipulate CIN ﬁring are not physiologically relevant, (ii)
CINs do not impact basal ganglia-related behaviors in
physiological conditions and/or (iii) the behavioral tasks used
are not appropriate to reveal CIN functions in rodents. What we
know about the function of CINs comes from studies carried out
in primates, describing the correlative changes in electrical
activity of presumed-CINs during behavior. Optogenetics,
mainly applied in rodents for technical reasons, is perfectly
suited to go beyond correlational analysis and to investigate
the causal implication of CINs in behavior. However, we ﬁrst need
to accurately describe the ﬁring properties of these cells in rodents
to be able to manipulate their activity in an appropriate way.

ACTIVITY OF CHOLINERGIC
INTERNEURONS DURING BEHAVIOR

The identiﬁcation of CINs in behaving animals is usually based on
their unique in vivo extracellular ﬁring activity (i.e. tonically active
at 5 spikes/s, sometimes in a burst mode) and broad spike
waveform (i.e. spike duration > 2 ms). These electrical properties
are easily distinguishable from all the other striatal cell populations
and represent a good signature of CINs as conﬁrmed later by
in vivo juxtacellular labelling (Inokawa et al., 2010; Sharott et al.,
2012). Using these classiﬁcation criteria, early studies ﬁrst deﬁned
the pattern of CINs activity during classical conditioning. In these
experiments, animals have to learn the association between a
neutral stimulus (i.e. often a tone) and an unexpected reward. In
this context, CINs classically respond with a pause in ﬁring that
occurs shortly after the conditioned stimulus and lasts around 200
ms. This pause can also be preceded and/or followed by excitatory
burst responses (Kimura et al., 1984; Aosaki, 1994; Apicella, 2017).

Interestingly, this stereotypical pause appears during learning
(Aosaki, 1994) and is time-locked to the response of nigral
dopaminergic neurons (Morris et al., 2004). It is also dependent
on the integrity of both dopaminergic neurons (Aosaki et al., 1994;
Raz et al., 1996) and glutamatergic inputs coming from the
intralaminar thalamus (Matsumoto et al., 2001).

What is not yet clear is whether the pause and burst
components carry different signals used to underlie speciﬁc
functions (Apicella, 2002; Apicella, 2007). Importantly, these
activity patterns are mostly synchronized in the CINs population
(Raz et al., 1996) such that they might efﬁciently translate into
global change of striatal ACh level, providing a temporal window
for complex pre- and post-synaptic modiﬁcations of striatal
network and plastic changes (Deffains and Bergman, 2015; Cox
and Witten, 2019). As a consequence, the pause response of CINs
is considered as a key cellular substrate for reward-based
learning, and may be particularly important for stimulus-
response and action-outcome associations. The exact cellular
and network explanations underlying the generation of the
pause/burst ﬁring responses are not known precisely. Multiple
mechanisms have been proposed to generate these responses.
They all have in common the capacity to broadcast efﬁciently the
information to spatially-distributed CINs (Goldberg and
Reynolds, 2011; Schulz and Reynolds, 2013; Zhang and Cragg,
2017). Such broadcast mechanisms include:

a) a change in intrinsic excitability driven by excitatory synaptic
inputs (Oswald et al., 2009; Ding et al., 2010; Doig et al., 2014;
Zhang et al., 2018; Reynolds et al., 2004). This scenario has
been well described for cortical and intralaminar nucleus
thalamic inputs but whether it can occur from any other
known glutamatergic sources [such as the one coming from
the pedonculopontine nucleus (Assous et al., 2019)] remained
to be addressed.

b) a putative effect of DA directly onto CINs (Yan et al., 1997;

Maurice, 2004; Yan and Surmeier, 1997).

c) a cholinergic input coming from the pedunculopontine and
laterodorsal tegmental nuclei that synapse preferentially with
CINs and give rise to excitatory responses (Dautan, 2014;
Dautan, 2018).

d) a direct inhibitory inputs coming from striatal GABAergic
interneurons surrounding MSNs (Gonzales et al., 2013).
Activation of one CIN is, for example, able to inhibit the
ﬁring of nearby CINs via nicotinic excitation of striatal
GABAergic interneurons. This microcircuit allows a wide-
spread inhibition of CINs by recurrent inhibition (Sullivan
et al., 2008; Faust et al., 2016).

Also, external sources such as GABAergic neurons from the
midbrain, or from the globus pallidus (GP), or from unknown
origin might also synchronize CIN population (Zhang and
Cragg, 2017). Among these GABAergic sources, the inhibitory
inputs coming from GP neurons appear to be functionally
efﬁcient at inducing a pause in CINs (Klug et al., 2018).
However, it is important to mention that the pallido-striatal
inputs could originate from two main populations of GP
neurons, namely the prototypic and the arkypallidal neurons

Frontiers in Pharmacology | www.frontiersin.org

3

December 2019 | Volume 10 | Article 1488

Mallet et al.

Investigating CIN Functional Role

(Mallet, 2012), and that the respective contribution of
arkypallidal or prototypic neurons in the CIN pause response
have not yet been assessed. That being said, anatomical evidences
would argue that arkypallidal neurons represent a good cellular
substrate to generate a synchronized pause in CIN ﬁring. Indeed,
arkypallidal neurons provide widespread striatal GABAergic
inhibition (Mallet, 2012; Mallet, 2016) that densely target, with
“basket-like” perisomatic contacts, the soma and proximal
dendrites of CINs (Mallet, 2012). It should also be noted that CINs
represent preferential targets for arkypallidal neurons, as suggested
by the larger number of apposition that a single-labeled arkypallidal
cells make onto CINs (Mallet, 2012). Altogether, we propose that
GABAergic arkypallidal neurons constitute a powerful mechanism
to generate synchronized inhibitory responses in CINs population.
Whether this arkypallidal-CINs circuit is part of a feed-back or a
feed-forward loop is not known but should be addressed in
future studies.

Apart from the classical conditioning experiments, the
contribution of CIN activity has also been tested during
operant tasks. In these experiments, the animal has to execute
an action to obtain a reward. These studies have revealed the
involvement of CINs in more complex behavioral aspects such as
contextual (Apicella, 2007), temporal (Morris et al., 2004), goal-
directed action (Bradﬁeld et al., 2013), sensori-motor gating
(Ding et al., 2010), movement control/modulation (Yarom and
Cohen, 2011; Nougaret and Ravel, 2015; Lee et al., 2006), and
action inhibition (Lee et al., 2006). Interestingly, the expression
of the pause in CIN ﬁring is largely dependent on the behavioral
task paradigm (Benhamou et al., 2014). This might actually
explain some of the discrepancies originally found between
monkey and rodent recordings.

In addition, recent works have taken advantage of transgenic
ChAT-Cre mice to genetically identify CINs and record their
activity with two-photon calcium imaging and ﬁber photometry,
during spontaneous locomotion in head-ﬁxed animals (Gritton,
2019; Howe, 2019; Rehani, 2019). In doing so, novel features of
CIN contributions to global
locomotion control have been
described. In particular, one study found that CINs increase
their activity during behavioral state transition, and could thus
favor the transition from one behavioral state to another (Howe,
2019). Alternatively, CINs activation can reduce ongoing
movement while synchronizing the activity of MSNs (Gritton,
2019). This synchronizing effect on striatal neurons is a
remarkable feature especially considering that excessive
expression of synchronized oscillatory activity in the beta
frequency band (12–30 Hz) is a hallmark associated with PD
and possibly linked to akinesia/bradykinesia in PD patients
(Brown, 2007) [but see (Nambu et al., 2015; McGregor and
Nelson, 2019)]. This further adds to the view that CIN
dysfunctional activity contributes to the pathophysiology of PD.
Indeed, there is good evidence to suggest that the loss of DA in
the striatum modiﬁes the cholinergic signalling (Tanimura, 2018;
McKinley, 2019; Ztaou and Amalric, 2019) and increases the
correlated activity between CINs (Raz, 2001). Although the
minimal neuronal circuit generating the parkinsonian beta
synchronizations in basal ganglia circuits are not known, it is

possible that CIN activity represents a good candidate to promote
synchronized activity in these neuronal networks. Indeed,
cholinergic agonist infusion in the striatum (McCarthy, 2011)
and optogenetic excitation of CINs (Kondabolu, 2016) can induce
an increase in the expression of beta oscillations. In addition,
CINs opto-excitation in normal animals generates parkinsonian-
like motor deﬁcits (Kondabolu, 2016) while CINs opto-inhibition
in PD mice decreases motor symptoms (Maurice, 2015).

EXPLORING CHOLINERGIC
INTERNEURONS FUNCTIONS IN BASAL
GANGLIA NETWORK: CONTRIBUTION OF
COMPUTATIONAL MODELING

CINs modulate striatal activity during behavior. A theoretical study
of the putative function of these neurons in motor learning and their
possible role in pathophysiology through modeling could drive
experimentally testable predictions and thereby guide further
experimental investigation. Previous modeling efforts involving
CINs remain relatively sparse. They range from simulating
intracellular and ion-channel dynamics linked to cholinergic
signaling to the effect of CIN activity modulation on behavior.

On the microscopic scale, two modeling studies have
highlighted the tight coupling between DA neurons and CINs
due to the dopaminergic modulation of both the intrinsic
currents generating tonic ﬁring (Aosaki et al., 1998; Maurice,
2004; Wilson and Goldberg, 2006; Deng et al., 2007) and the
external inputs to CINs (Nicola et al., 2000; Pisani et al., 2000).
Szalisznyó and Müller (2009) analyzed conductance-based
changes in CIN subthreshold oscillations induced by DA and
predicted that DA can switch CINs between stable oscillatory
and ﬁxed-point behaviors, with opposing effects of D1- and D2-
type dopamine receptors. Tan and Bullock (2008) have shown
that DA inputs robustly cooperate with thalamic inputs to control
cue-dependent CIN pauses. Thereby, DA strongly affects
performance- and learning-related dynamics in the striatum. The
DA-CINs coupling could explain the adaptively scaled DA burst and
the CIN burst and pause observed experimentally in response to
reward-predicting cues. These changes would thus not necessarily
require a modiﬁcation in the weight of synapses onto CINs.

On the macroscopic scale, the inﬂuence of CINs on behavior
can be either immediate, due to the modulation of striatal output
by CINs, or delayed/persistent, due to ACh-dependent plasticity
in the striatal network that leads to long-term changes in striatal
response to its external inputs. A recent study by Vogt and
Hofmann (2012) modeled the modulation in the activity of DA
neurons and CINs in relation to external reward delivery and its
internal expectation. They show that activity changes and their
effect on learning outcome can be explained by a direct effect of
neuromodulators (DA and ACh) on postsynaptic activity, even
with unmodulated, two-factor spike timing-dependent plasticity
(STDP). Obviously, it does not prohibit joint operation together
with three-factor STDP rules. Interestingly, CIN pause could
represent a time window to gate phasic DA release and “bracket”

Frontiers in Pharmacology | www.frontiersin.org

4

December 2019 | Volume 10 | Article 1488

Mallet et al.

Investigating CIN Functional Role

the plasticity window, while DA variations reciprocally modulate
the CIN pause duration to adjust this window (Kim, 2019). In the
context of reward-based motor adaptation, phasic DA release
could thereby deliver reward information for reinforcement
learning in a timely manner. Changes in CIN-DA interactions
due to DA depletion would then produce poor performance of
motor adaptation. Alternatively, CINs could act mainly on MSNs
to suppress their ﬁring and regulate local inhibitory network
(Ashby and Crossley, 2011; Franklin and Frank, 2015).

To go beyond this current state of theoretical investigations,
one may ask the following questions. What are the respective/
speciﬁc roles of DA and ACh during learning? How redundant
are these signals? Are they separable in time or space? What is
the speciﬁc motor impairment expected due to the abnormal
CIN activity following DA depletion and could some
PD symptoms be linked to CIN signaling dysfunction? These
questions may be answered by integrating current experimental
evidence and DA-ACh interactions and its effect on striatal
dynamics revealed by previous theoretical work in a circuit
model of the basal ganglia-thalamo-cortical loop. This model
may display action selection properties and DA-driven
reinforcement learning (Leblois et al., 2006; Guthrie et al.,
2013), as well as PD-related dysfunction under DA depletion.
The computational advantages brought by CINs and the neural
mechanisms can be investigated in such a theoretical framework.
Speciﬁc predictions can then be derived from model concerning
the effects of manipulating CIN activity in a reinforcement
learning protocol. These predictions could eventually be
tested experimentally with physiological recordings performed
in an operant conditioning task to ensure that the suggested
mechanisms are indeed at play in the striatum during
motor learning.

REFERENCES

Abudukeyoumu, N., Hernandez-Flores, T., Garcia-Munoz, M., and Arbuthnott,
G. W. (2019). Cholinergic modulation of striatal microcircuits. Eur. J. Neurosci.
49, 604–622. doi: 10.1111/ejn.13949

Aosaki, T., Tsubokawa, H., Ishida, A., Watanabe, K., Graybiel, A., and Kimura, M.
(1994). Effect of the nigrostriatal dopamine system on acquired neural
responses in the striatum of behaving monkeys. Science 265, 412–415. doi:
10.1126/science.8023166

Aosaki, T., Kimura, M., and Graybiel, A. M. (1995). Temporal and spatial
characteristics of tonically active neurons of the primate's striatum.
J. Neurophysiol. 73, 1234–1252. doi: 10.1152/jn.1995.73.3.1234

Aosaki, T., Kiuchi, K., and Kawaguchi, Y. (1998). Dopamine D1-like receptor
activation excites rat striatal large aspiny neurons in vitro. J. Neurosci. 18,
5180–5190. doi: 10.1523/JNEUROSCI.18-14-05180.1998

Aosaki, T., Tsubokawa, H., Ishida, A., Watanabe, K., Graybiel, A. M., and Kimura, M.
(1994). Responses of tonically active neurons in the primate's striatum undergo
systematic changes during behavioral sensorimotor conditioning. J. Neurosci. 14,
3969–3984. doi: 10.1523/JNEUROSCI.14-06-03969.1994

Apicella, P. (2002). Tonically active neurons in the primate striatum and their role
in the processing of information about motivationally relevant events. Eur. J.
Neurosci. 16, 2017–2026. doi: 10.1046/j.1460-9568.2002.02262.x

Apicella, P. (2007). Leading tonically active neurons of the striatum from reward
detection to context recognition. Trends Neurosci. 30, 299–306. doi: 10.1016/
j.tins.2007.03.011

CONCLUDING REMARKS

Our current understanding of the role of CINs in striatal function
derives mostly from extracellular recordings of TANs in monkeys.
Because these neurons transiently respond to motivationally
relevant cues with brief pauses, ﬂanked by bursts of increased
activity, they are classically viewed as key players in reward
related learning. However, how CINs, and particularly the pause
in their tonic ﬁring, modulate striatal output has yet to be
demonstrated. It is also undisputable that CINs play a key role in
relation to dysfunctional aspect of basal ganglia information
processing such as in PD and it seems important that future
works keep dissecting the causal role of CINs in striatal circuits.

AUTHOR CONTRIBUTIONS

NMal, AL, NMau, and CB drafted, provided critical revision of
the article, wrote, and approved the ﬁnal version of the review.

ACKNOWLEDGMENTS

This work was supported by grants from the French Agence
Nationale de la Recherche (ANR-2010-1416, ANR-14-CE13-
0024-01, ANR-15-CE37-0006 and ANR-16-CE37-0020-01),
Fondation de France (# 146280), France Parkinson nonproﬁt
organization (OPE-2018-0459), and the LABEX BRAIN (ANR-
10-LABX-43). We thank Nuno Miguel Luis for the
manuscript proofreading.

Apicella, P. (2017). The role of the intrinsic cholinergic system of the striatum:
what have we learned from TAN recordings in behaving animals? Neuroscience
360, 81–94. doi: 10.1016/j.neuroscience.2017.07.060

Ashby, F. G., and Crossley, M. J. (2011). A computational model of how
cholinergic interneurons protect striatal-dependent learning. J. Cogn.
Neurosci. 23, 1549–1566. doi: 10.1162/jocn.2010.21523

Assous, M., Dautan, D., Tepper, J. M., and Mena-Segovia, J. (2019).
Pedunculopontine glutamatergic neurons provide a novel source of
feedforward inhibition in the striatum by selectively targeting interneurons.
J. Neurosci. 39, 4727–4737. doi: 10.1523/JNEUROSCI.2913-18.2019

Barbeau, A. (1962). The pathogenesis of Parkinson's disease: a new hypothesis.

Can. Med. Assoc. J. 87, 802–807.

Benhamou, L., Kehat, O., and Cohen, D. (2014). Firing pattern characteristics of
tonically active neurons in rat striatum: context dependent or species
divergent? J. Neurosci. 34, 2299–2304. doi: 10.1523/JNEUROSCI.1798-13.2014
Bennett, B. D., Callaway, J. C., and Wilson, C. J. (2000). Intrinsic membrane properties
underlying spontaneous tonic ﬁring in neostriatal cholinergic interneurons. J.
Neurosci. 20, 8493–8503. doi: 10.1523/JNEUROSCI.20-22-08493.2000

Bolam, J. P., Wainer, B. H., and Smith, A. D. (1984). Characterization of
cholinergic neurons in the rat neostriatum. A combination of choline
acetyltransferase immunocytochemistry, Golgi-impregnation and electron
microscopy. Neuroscience 12, 711–718. doi: 10.1016/0306-4522(84)90165-9
Bradﬁeld, L. A., Bertran-Gonzalez, J., Chieng, B., and Balleine, B. W. (2013). The
thalamostriatal pathway and cholinergic control of goal-directed action:
interlacing new with existing learning in the striatum. Neuron 79, 153–166.
doi: 10.1016/j.neuron.2013.04.039

Frontiers in Pharmacology | www.frontiersin.org

5

December 2019 | Volume 10 | Article 1488

Mallet et al.

Investigating CIN Functional Role

Brown, P. (2007). Abnormal oscillatory synchronisation in the motor system leads
to impaired movement. Curr. Opin. Neurobiol. 17, 656–664. doi: 10.1016/
j.conb.2007.12.001

Cox, J., and Witten, I. B. (2019). Striatal circuits for reward learning and decision-
making. Nat. Rev. Neurosci. 20, 482–494. doi: 10.1038/s41583-019-0189-2
Dautan, D., Huerta-Ocampo, I., Valencia, M., Kondabolu, K. , Gerdjikov, T. V. ,
and Mena-Segovia, J. (2014). A major external source of cholinergic
innervation of the striatum and nucleus accumbens originates in the
brainstem. J. Neurosci. 34, 4509–4518. doi: 10.1523/JNEUROSCI.5071-13.2014
Dautan, D., Huerta-Ocampo, I., Valencia, M., Kondabolu, K., Gerdjikov, T. V., and
Mena-Segovia, J. (2018). Cholinergic midbrain afferents modulate striatal circuits
and shape encoding of action control. bioRxiv. doi: 10.1101/388223388223
Deffains, M., and Bergman, H. (2015). Striatal cholinergic interneurons and
cortico-striatal synaptic plasticity in health and disease. Mov. Disord. 30,
1014–1025. doi: 10.1002/mds.26300

Deng, P., Zhang, Y., and Xu, Z. C. (2007). Involvement of Ih in dopamine
modulation of tonic ﬁring in striatal cholinergic interneurons. J. Neurosci. 27,
3148–3156. doi: 10.1523/JNEUROSCI.5535-06.2007

Ding, J. B., Guzman, J. N., Peterson, J. D., Goldberg, J. a., and Surmeier, D. J.
(2010). Thalamic gating of corticostriatal signaling by cholinergic
interneurons. Neuron 67, 294–307. doi: 10.1016/j.neuron.2010.06.017

Ding, J., Guzman, J. N., Tkatch, T., Chen, S., Goldberg, J. A., Erbert, P. J., et al.
(2006). RGS4-dependent attenuation of M4 autoreceptor function in striatal
cholinergic interneurons following dopamine depletion. Nat. Neurosci. 9, 832–
842. doi: 10.1038/nn1700

Doig, N. M., Magill, P. J., Apicella, P., Bolam, J. P., and Sharott, A. (2014). Cortical
and thalamic excitation mediate the multiphasic responses of striatal
cholinergic interneurons to motivationally salient stimuli. J. Neurosci. 34,
3101–3117. doi: 10.1523/JNEUROSCI.4627-13.2014

English, D. F., Ibanez-Sandoval, O., Stark, E., Tecuapetla, F., Buzsáki, G.,
Deisseroth, K., et al. (2011). GABAergic circuits mediate the reinforcement-
related signals of striatal cholinergic interneurons. Nat. Neurosci. 15, 123–130.
doi: 10.1038/nn.2984

Faust, T. W., Assous, M., Tepper, J. M., and Koós, T. (2016). Neostriatal
GABAergic interneurons mediate cholinergic inhibition of spiny projection
neurons. J. Neurosci. 36, 9505–9511. doi: 10.1523/JNEUROSCI.0466-16.2016
Franklin, N. T., and Frank, M. J. (2015). A cholinergic feedback circuit to regulate
striatal population uncertainty and optimize reinforcement learning. Elife 4,
e12029. doi: 10.7554/eLife.12029

Goldberg, J. A., and Reynolds, J. N. J. (2011). Spontaneous ﬁring and evoked
pauses in the tonically active cholinergic interneurons of the striatum.
Neuroscience 198, 27–43. doi: 10.1016/j.neuroscience.2011.08.067

Gonzales, K. K., Pare, J. F., Wichmann, T., and Smith, Y. (2013). GABAergic
inputs from direct and indirect striatal projection neurons onto cholinergic
interneurons in the primate putamen. J. Comp. Neurol. 521, 2502–2522. doi:
10.1002/cne.23295

Gritton, H. J., Howe, H. M., Romano, M. F., DiFeliceantonio, A. G., Kramer, M. A.,
Saligrama, V., et al. (2019). Unique contributions of parvalbumin and
cholinergic interneurons in organizing striatal networks during movement.
Nat. Neurosci. 22, 586–597. doi: 10.1038/s41593-019-0341-3

Guthrie, M., Leblois, A., Garenne, A., and Boraud, T. (2013). Interaction between
cognitive and motor cortico-basal ganglia loops during decision making:
a computational study. J. Neurophysiol. 109, 3025–3040. doi: 10.1152/
jn.00026.2013

Hersch, S. M., Gutekunst, C. A., Rees, H. D., Heilman, C. J., and Levey, A. I. (1994).
Distribution of m1-m4 muscarinic receptor proteins in the rat striatum: light and
electron microscopic immunocytochemistry using subtype-speciﬁc antibodies.
J. Neurosci. 14, 3351–3363. doi: 10.1523/JNEUROSCI.14-05-03351.1994

Higley, M. J., Soler-Llavina, G. J., and Sabatini, B. L. (2009). Cholinergic
modulation of multivesicular release regulates striatal synaptic potency and
integration. Nat. Neurosci. 12, 1121–1128. doi: 10.1038/nn.2368

Howe, W. M., Young, D. A., Bekheet, G., and Kozak, R. (2016). Nicotinic receptor
subtypes differentially modulate glutamate release in the dorsal medial
striatum. Neurochem. Int. 100, 30–34. doi: 10.1016/j.neuint.2016.08.009
Howe, M., Ridouh, I., Allegra Mascaro, A. L., Larios, A., Azcorra, M., Dombeck, D. A.,
et al. (2019). Coordination of rapid cholinergic and dopaminergic signaling in
striatum during spontaneous movement. Elife 28 (8), e44903. doi: 10.7554/
eLife.44903

Inokawa, H., Yamada, H., Matsumoto, N., Muranishi, M., and Kimura, M. (2010).
Juxtacellular labeling of tonically active neurons and phasically active neurons
in the rat striatum. Neuroscience 168, 395–404. doi: 10.1016/j.neuroscience.
2010.03.062

Kim, T., Capps, R. A., Hamade, K. C., Barnett, W. H., Todorov, D. I., Latash, E. M.,
et al. (2019). The functional role of striatal cholinergic interneurons in
reinforcement learning from computational perspective. Front. Neural
Circuits 13, 10. doi: 10.3389/fncir.2019.00010

Kimura, M., Rajkowski, J., and Evarts, E. (1984). Tonically discharging putamen
neurons exhibit set-dependent responses. Proc. Natl. Acad. Sci. U. S. A. 81,
4998–5001. doi: 10.1073/pnas.81.15.4998

Klug, J. R., Engelhardt, M. D., Cadman, C. N., Li, H., Smith, J. B., Ayala, S., et al.
(2018). Differential inputs to striatal cholinergic and parvalbumin interneurons
imply functional distinctions. elife, 7, e35657.

Kondabolu, K., Roberts, E. A., Bucklin, M., McCarthy, M. M., Kopell, N., and Han,
X. (2016). Striatal cholinergic interneurons generate beta and gamma
oscillations in the corticostriatal circuit and produce motor deﬁcits. Proc.
Natl. Acad. Sci. 113, E3159–E3168. doi: 10.1073/pnas.1605658113

Leblois, A., Boraud, T., Meissner, W., Bergman, H., and Hansel, D. (2006).
Competition between feedback loops underlies normal and pathological
dynamics in the Basal Ganglia. J. Neurosci. 26, 3567–3583. doi: 10.1523/
JNEUROSCI.5050-05.2006

Lee, I. H., Seitz, A. R., and Assad, J. A. (2006). Activity of tonically active neurons
in the monkey putamen during initiation and withholding of movement.
J. Neurophysiol. 95, 2391–2403. doi: 10.1152/jn.01053.2005

Lerner, T. N., and Kreitzer, A. C. (2011). Neuromodulatory control of striatal
plasticity and behavior. Curr. Opin. Neurobiol. 21, 322–327. doi: 10.1016/
j.conb.2011.01.005

Lovinger, D. M. (2010). Neurotransmitter roles in synaptic modulation, plasticity
and learning in the dorsal striatum. Neuropharmacology 58, 951–961. doi:
10.1016/j.neuropharm.2010.01.008

Lozovaya, N., Eftekhari, S., Cloarec, R., Gouty-Colomer, L. A., Dufour, A., Riffault,
B., et al. (2018). GABAergic inhibition in dual-transmission cholinergic and
GABAergic striatal
interneurons is abolished in Parkinson disease. Nat.
Commun. 9, 1422. doi: 10.1038/s41467-018-03802-y

Mallet, N., Micklem, B. R., Henny, P., Brown, M. T., Williams, C., Bolam, J. P.,
et al. (2012). Dichotomous organization of the external globus pallidus. Neuron
74, 1075–1086. doi: 10.1016/j.neuron.2012.04.027

Mallet, N., Schmidt, R., Leventhal, D., Chen, F., Amer, N., Boraud, T., et al. (2016).
Arkypallidal cells send a stop signal to striatum. Neuron 89, 308–316. doi:
10.1016/j.neuron.2015.12.017

Matsumoto, N., Minamimoto, T., Graybiel, A. M., and Kimura, M. (2001).
Neurons in the thalamic CM-Pf complex supply striatal neurons with
information about behaviorally signiﬁcant sensory events. J. Neurophysiol.
85, 960–976. doi: 10.1152/jn.2001.85.2.960

Maurice, N., Mercer, J., Chan, C. S., Hernandez-Lopez, S., Held, J., Tkatch, T., et al.
(2004). D2 dopamine receptor-mediated modulation of voltage-dependent Na
+ channels reduces autonomous activity in striatal cholinergic interneurons. J.
Neurosci. 24, 10289–10301. doi: 10.1523/JNEUROSCI.2155-04.2004

Maurice, N., Liberge, M., Jaouen, F., Ztaou, S., Hanini, M., Camon, J., et al. (2015).
Striatal cholinergic interneurons control motor behavior and basal ganglia
function in experimental parkinsonism. Cell Rep. 13, 657–666. doi: 10.1016/
j.celrep.2015.09.034

McCarthy, M. M., Moore-Kochlacs, C., Gu, X., Boyden, E. S., Han, X., Kopell, N.,
et al. (2011). Striatal origin of the pathologic beta oscillations in Parkinson's
disease. Proc. Natl. Acad. Sci. 108, 11620–11625. doi: 10.1073/pnas.1107748108
McGregor, M. M., and Nelson, A. B. (2019). Circuit Mechanisms of Parkinson's

Disease. Neuron 101, 1042–1056. doi: 10.1016/j.neuron.2019.03.004

McKinley, J. W., Shi, Z., Kawikova, I., Hur, M., Bamford, U., Sudarsana Devi, S. P.,
et al. (2019). Dopamine deﬁciency reduces striatal cholinergic interneuron
function in models of parkinson's disease. Neuron 103, 1056–1072.e6. doi:
10.1016/j.neuron.2019.06.013

Morris, G., Arkadir, D., Nevet, A., Vaadia, E., and Bergman, H. (2004). Coincident
but distinct messages of midbrain dopamine and striatal tonically active
neurons. Neuron 43, 133–143. doi: 10.1016/j.neuron.2004.06.012

Nambu, A., Tachibana, Y., and Chiken, S. (2015). Cause of parkinsonian
symptoms: ﬁring rate, ﬁring pattern or dynamic activity changes? Basal
Ganglia 5, 1–6. doi: 10.1016/j.baga.2014.11.001

Frontiers in Pharmacology | www.frontiersin.org

6

December 2019 | Volume 10 | Article 1488

Mallet et al.

Investigating CIN Functional Role

Nicola, S. M., Surmeier, D. J., and Malenka, R. C. (2000). Dopaminergic
modulation of neuronal excitability in the striatum and nucleus accumbens.
Annu. Rev. Neurosci. 23, 185–215. doi: 10.1146/annurev.neuro.23.1.185
Nougaret, S., and Ravel, S. (2015). Modulation of tonically active neurons of
the monkey striatum by events carrying different force and reward
information. J. Neurosci. 35, 15214–15226. doi: 10.1523/JNEUROSCI.0039-
15.2015

Oswald, M. J., Oorschot, D. E., Schulz, J. M., Lipski, J., and Reynolds, J. N. J. (2009).
IH current generates the afterhyperpolarisation following activation of
subthreshold cortical synaptic inputs to striatal cholinergic interneurons.
J. Physiol. 587, 5879–5897. doi: 10.1113/jphysiol.2009.177600

Pakhotin, P., and Bracci, E. (2007). Cholinergic interneurons control the excitatory input
to the striatum. J. Neurosci. 27, 391–400. doi: 10.1523/JNEUROSCI.3709-06.2007
Pisani, A., Bonsi, P., Centonze, D., Calabresi, P., and Bernardi, G. (2000).
Activation of D2-like dopamine receptors reduces synaptic inputs to striatal
cholinergic interneurons. J. Neurosci. 20, RC69 1–RC69 6. doi: 10.1523/
JNEUROSCI.20-07-j0003.2000

Raz, A., Feingold, A., Zelanskaya, V., Vaadia, E., and Bergman, H. (1996). Neuronal
synchronization of tonically active neurons in the striatum of normal and
parkinsonianprimates.J.Neurophysiol.76,2083–2088.doi:10.1152/jn.1996.76.3.2083
Raz, A., Frechter-Mazar, V., Feingold, A., Abeles, M., Vaadia, E., Bergman, H.,
et al. (2001). Activity of pallidal and striatal tonically active neurons is
correlated in mptp-treated monkeys but not in normal monkeys. J. Neurosci.
21, RC128 1–5. doi: 10.1523/JNEUROSCI.21-03-j0006.2001

Rehani, R., Atamna, Y., Tiroshi, L., Chiu, W. H., de Jesús Aceves Buendía, J., Martins,
G. J., et al. (2019). Activity patterns in the neuropil of striatal cholinergic
interneurons in freely moving mice represent their collective spiking dynamics.
Eneuro 6 (1), ENEURO.0351–18.2018. doi: 10.1523/ENEURO.0351-18.2018
Reynolds, J. N. J., Hyland, B. I., and Wickens, J. R. (2004). Modulation of an
afterhyperpolarization by the substantia nigra induces pauses in the tonic ﬁring
of striatal cholinergic interneurons. J. Neurosci. 24, 9870–9877. doi: 10.1523/
JNEUROSCI.3225-04.2004

Salin, P., López, I. P., Kachidian, P., Barroso-Chinea, P., Rico, A. J., Gómez-
Bautista, V., et al. (2009). Changes to interneuron-driven striatal microcircuits
in a rat model of Parkinson's disease. Neurobiol. Dis. 34, 545–552. doi: 10.1016/
j.nbd.2009.03.006

Schulz, J. M., and Reynolds, J. N. J. (2013). Pause and rebound: sensory control of
cholinergic signaling in the striatum. Trends Neurosci. 36, 41–50. doi: 10.1016/
j.tins.2012.09.006

Sharott, A., Doig, N. M., Mallet, N., and Magill, P. J. (2012). Relationships between
the ﬁring of identiﬁed striatal interneurons and spontaneous and driven
cortical activities in vivo. J. Neurosci. 32, 13221–13236. doi: 10.1523/
JNEUROSCI.2440-12.2012

Sullivan, M. A., Chen, H., and Morikawa, H. (2008). Recurrent inhibitory network
among striatal cholinergic interneurons. J. Neurosci. 28, 8682–8690. doi:
10.1523/JNEUROSCI.2411-08.2008

Szalisznyó, K., and Müller, L. (2009). Dopamine induced switch in the
subthreshold dynamics of the striatal cholinergic interneurons: a numerical
study. J. Theor. Biol. 256, 547–560. doi: 10.1016/j.jtbi.2008.09.029

Tan, C. O., and Bullock, D. (2008). A dopamine–acetylcholine cascade: simulating
learned and lesion-induced behavior of striatal cholinergic interneurons.
J. Neurophysiol. 100, 2409–2421. doi: 10.1152/jn.90486.2008

Tanimura, A., Pancani, T., Lim, S. A. O., Tubert, C., Melendez, A. E., Shen, W.,
et al. (2018). Striatal cholinergic interneurons and Parkinson's disease. Eur. J.
Neurosci. 47, 1148–1158. doi: 10.1111/ejn.13638

Tozzi, A., de Iure, A., Di Filippo, M., Tantucci, M., Costa, C., Borsini, F., et al. (2011).
The distinct role of medium spiny neurons and cholinergic interneurons in the D2/
A2A receptor interaction in the striatum: implications for Parkinson's Disease.
J. Neurosci. 31, 1850–1862. doi: 10.1523/JNEUROSCI.4082-10.2011

Vogt, S. M., and Hofmann, U. G. (2012). Neuromodulation of STDP through
short-term changes in ﬁring causality. Cogn. Neurodyn. 6, 353–366. doi:
10.1007/s11571-012-9202-4

Wang, Z., Kai, L., Day, M., Ronesi, J., Yin, H. H., Ding, J., et al. (2006).
Dopaminergic control of corticostriatal
long-term synaptic depression in
medium spiny neurons is mediated by cholinergic interneurons. Neuron 50,
443–452. doi: 10.1016/j.neuron.2006.04.010

Weiner, D. M., Levey, A. I., and Brann, M. R. (1990). Expression of muscarinic
acetylcholine and dopamine receptor mRNAs in rat basal ganglia. Proc. Natl.
Acad. Sci. 87, 7050–7054. doi: 10.1073/pnas.87.18.7050

Wilson, C. J., and Goldberg, J. A. (2006). Origin of the slow afterhyperpolarization
and slow rhythmic bursting in striatal cholinergic interneurons.
J. Neurophysiol. 95, 196–204. doi: 10.1152/jn.00630.2005

Yan, Z., and Surmeier, D. J. (1997). D5 dopamine receptors enhance Zn2+-sensitive
GABA(A) currents in striatal cholinergic interneurons through a PKA/PP1
cascade. Neuron 19, 1115–1126. doi: 10.1016/S0896-6273(00)80402-X

Yan, Z., Song, W.-J., and Surmeier, D. J. D. (1997). 2 Dopamine receptors reduce
N-Type Ca 2+ currents in rat neostriatal cholinergic interneurons through a
membrane-delimited, protein-kinase-c-insensitive pathway. J. Neurophysiol.
77, 1003–1015. doi: 10.1152/jn.1997.77.2.1003

Yarom, O., and Cohen, D. (2011). Putative cholinergic interneurons in the ventral
and dorsal regions of the striatum have distinct roles in a two choice alternative
association task. Front. Syst. Neurosci. 5, 36. doi: 10.3389/fnsys.2011.00036
Zhang, Y.-F., and Cragg, S. J. (2017). Pauses in striatal cholinergic interneurons:
what is revealed by their common themes and variations? Front. Syst. Neurosci.
11, 1–8. doi: 10.3389/fnsys.2017.00080

Zhang, Y. F., Reynolds, J. N. J., and Cragg, S. J. (2018). Pauses in cholinergic
interneuron activity are driven by excitatory input and delayed rectiﬁcation,
with dopamine modulation. Neuron 98, 918–925.e3. doi: 10.1016/
j.neuron.2018.04.027

Ztaou, S., and Amalric, M. (2019). Contribution of cholinergic interneurons to
striatal pathophysiology in Parkinson's disease. Neurochem. Int. 126, 1–10. doi:
10.1016/j.neuint.2019.02.019

Ztaou, S., Lhost, J., Watabe, I., Torromino, G., and Amalric, M. (2018). Striatal
cholinergic interneurons regulate cognitive and affective dysfunction in partially
dopamine-depleted mice. Eur. J. Neurosci. 48, 2988–3004. doi: 10.1111/ejn.14153
Zucca, S., Zucca, A., Nakano, T., Aoki, S., and Wickens, J. (2018). Pauses in
cholinergic interneuron ﬁring exert an inhibitory control on striatal output in
vivo. Elife 7, e32510. doi: 10.7554/eLife.32510

Conﬂict of Interest: The authors declare that the research was conducted in the
absence of any commercial or ﬁnancial relationships that could be construed as a
potential conﬂict of interest.

Copyright © 2019 Mallet, Leblois, Maurice and Beurrier. This is an open-access
article distributed under the terms of the Creative Commons Attribution License
(CC BY). The use, distribution or reproduction in other forums is permitted, pro-
vided the original author(s) and the copyright owner(s) are credited and that the
original publication in this journal is cited, in accordance with accepted academic
practice. No use, distribution or reproduction is permitted which does not comply
with these terms.

Frontiers in Pharmacology | www.frontiersin.org

7

December 2019 | Volume 10 | Article 1488

