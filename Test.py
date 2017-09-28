def jsonToList(dic):
    jsonList = []
    for key, value in dic.items():
        if str(key).isdigit():
            jsonList.append(str(key + '  ' + value))
        else:
            jsonList.append(str(key))
            if type(value) == dict:
                jsonList.extend(jsonToList(value))
            else:
                jsonList.append(str(value))

    return jsonList


dic = {"body": {"50": "prefer a free-carrier state, and can only be trapped near oxygen vacancies or form shallow donor states", "49": "atom, forming a small polaron, which can easily hop to neighboring sites. In contrast, electrons in anatase", "52": "and indicates that even small structural variations in the crystal lattice can lead to a very different behavior.", "24": "with a \u22483 eV band gap. TiO2 can be turned into an", "25": "n-type semiconductor by adding excess electrons by", "26": "various means\u2014doping, UV irradiation, or chemical reduc-", "27": "tion. Electrons in the conduction band of TiO2 compete", "20": "of research, a consensus on the origin of the difference", "21": "between the two materials is still absent, and our aim is to", "22": "resolve this issue theoretically as well as experimentally.", "23": "Stoichiometric rutile and anatase are both insulators", "46": "A combination of scanning tunneling microscopy and spectroscopy and density functional theory is used", "47": "to characterize excess electrons in TiO2 rutile and anatase, two prototypical materials with identical", "48": "chemical composition but different crystal lattices. In rutile, excess electrons can localize at any lattice Ti", "28": "between free-carrier and polaronic configurations. The", "29": "extent to which this happens has remained highly con-", "1": "importance in virtually all applications of these materials.", "0": "The behavior of charge carriers in oxides is of key", "3": "an oxide, they may either retain the free-carrier character or,", "2": "When excess electrons are added to the conduction band of", "5": "tortions induced by its presence (electron-phonon inter-", "4": "still assuming a defect-free crystal, couple to lattice dis-", "6": "action). The latter case is usually referred to as a small or", "13": "prototypical metal oxide. TiO2 is used in catalysis [5\u20138],", "12": "from first principles [3,4]. Here we investigate TiO2, a", "15": "and as a transparent conductive oxide [10]. Two forms of", "14": "photoelectrochemical (Gr\u00e4tzel) solar cells, memristors [9],", "17": "stable anatase form is generally present in nanomaterials", "16": "TiO2 are used industrially, rutile and anatase. The meta-", "19": "tions and in optoelectronics. Even after several decades", "18": "and shows better performance in energy-related applica-", "31": "properties and catalytic activity. The electrons can localize", "30": "troversial, yet strongly affects the material\u2019s transport", "51": "bound to Nb dopants. The present study conclusively explains the differences between the two polymorphs", "36": "lattice relaxations in its immediate surrounding is called a", "35": "The quasiparticle consisting of an electron coupled to the", "34": "ations of the surrounding lattice atoms by typically 0.1 \u00c5.", "33": "ions. This induces relax-", "32": "at Ti 3d orbitals, forming Ti3\u00fe"}, "NA": {"60": "3Materials Department, University of California, Santa Barbara, California 93106-5050, USA", "61": "", "62": "P H Y S I C A L R E V I E W L E T T E R S", "63": "(Received 20 January 2014; published 18 August 2014)", "64": "", "65": "Xianfeng Hao,1 Michael Schmid,1 Anderson Janotti,3", "66": "PACS numbers: 71.38.Ht, 68.47.Gh, 71.38.Fp, 73.20.At", "67": "small polaron [1]. When thermally activated, small polar-", "68": "ons exhibit hopping mobility. If the structural deformation", "69": "spreads over a large number of lattice sites the correspond-", "80": "bulk-terminated rutile (110)-(1 \u00d7 1) and anatase (101)-", "81": "(1 \u00d7 1) surfaces. In rutile, the excess electrons leave the", "86": "confined by the donor potential, yet they keep the bandlike", "87": "character.", "84": "show that", "85": "in Nb-doped anatase electrons are spatially", "104": "086402-1", "101": "required to distort the lattice (EST), and the electronic", "108": "\u00a9 2014 American Physical Society", "106": "week ending", "44": "", "45": "1Institute of Applied Physics, Vienna University of Technology, Wiedner Hauptstrasse 8-10/134, 1040 Vienna, Austria", "42": "", "43": "2Faculty of Physics and Center for Computational Materials Science, Universit\u00e4t Wien, Sensengasse 8/8-12, A-1090 Wien, Austria", "40": "", "41": "0031-9007=14=113(8)=086402(5)", "82": "VOs and form polarons, which can hop through the lattice.", "97": "TiO2 is sketched in Fig. 1(a). The formation energy, EPOL,", "7": "action). The latter case is usually referred to as a small or", "105": "", "8": "large polaron, depending on the degree of electron locali-", "96": "The energy balance for polaron formation in defect-free", "109": "", "83": "In anatase, the electrons stay trapped at the VOs. Finally, we", "100": "results from the competition between the strain energy", "77": "Next, we inspect the effect of excess electrons donated by", "76": "Ti site, while anatase prefers a free-carrier configuration.", "75": "We establish that rutile allows polaron formation at any", "74": "crystal, i.e., stoichiometric bulk cells of anatase and rutile.", "73": "intrinsic behavior of an excess electron added to the perfect", "72": "imental approach. First, we theoretically investigate the", "71": "Here we use the following joint theoretical and exper-", "70": "ing solution is categorized as a large polaron.", "91": "states STM images reflect the spatial distribution of electrons", "90": "microscopy and spectroscopy (STM/STS) was used. Filled-", "93": "the electronic energy EEL (see below): Either \u223c1 eV below", "92": "within the band gap, and STS provides information about", "95": "below EF for delocalized, weakly bound electrons [12].", "94": "Fermi level (EF) typical for small polarons [5], or \u223c40 meV", "79": "tal and density functional theory (DFT \u00fe U) data. We use", "78": "surface oxygen vacancies (VOs) by comparing experimen-", "99": "polaronic and fully delocalized free-carrier solution, and", "39": "PRL 113, 086402 (2014)", "38": "", "98": "is defined as the total energy difference between the", "55": "Martin Setvin,1,* Cesare Franchini,2,\u2020", "54": "", "56": "DOI: 10.1103/PhysRevLett.113.086402", "37": "lattice relaxations in its immediate surrounding is called a", "88": "For our calculations we used the VASP code [11]. On", "53": "and indicates that even small structural variations in the crystal lattice can lead to a very different behavior.", "107": "22 AUGUST 2014", "89": "the experimental side, low-temperature scanning tunneling", "103": "", "102": "energy gained by localizing the electron at a Ti site in such"}, "author": {"57": "Direct View at Excess Electrons in TiO2 Rutile and Anatase", "59": "3Materials Department, University of California, Santa Barbara, California 93106-5050, USA", "58": "Merzuk Kaltak,2 Chris G. Van de Walle,3 Georg Kresse,2 and Ulrike Diebold1"}, "title": {"9": "affect a materials\u2019 physical and chemical properties, yet", "10": "it remains controversial how to model", "12": "from first principles [3,4]. Here we investigate TiO2, a", "11": "it appropriately"}}
print jsonToList(dic)