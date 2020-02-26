import random

nouns = [
    ('Aal', 'm'), ('Abgottschlange', 'f'), ('Acerola', 'f'), ('Adler', 'm'), ('Admiral', 'm'),
    ('Affenbrotbaum', 'm'), ('Ahorn', 'm'), ('Akazie', 'f'), ('Albatros', 'm'), ('Alligator', 'm'),
    ('Alpaka', 'n'), ('Amarant', 'm'), ('Ameise', 'f'), ('Ameisenigel', 'm'), ('Amsel', 'f'),
    ('Ananas', 'f'), ('Anglerfisch', 'm'), ('Anis', 'm'), ('Antilope', 'f'), ('Apfelbaum', 'm'),
    ('Apfelbeere', 'f'), ('Apfel', 'm'), ('Aprikose', 'f'), ('Aprikosenbaum', 'm'),
    ('Archaeopteryx', 'm'),
    ('Arnika', 'f'), ('Aronia', 'f'), ('Artischocke', 'f'), ('Aubergine', 'f'), ('Auerhuhn', 'n'),
    ('Auerochse', 'm'), ('Auster', 'f'), ('Austernfischer', 'm'), ('Avocado', 'f'),
    ('Bachforelle', 'f'),
    ('Bachstelze', 'f'), ('Baldrian', 'm'), ('Banane', 'f'), ('Bandwurm', 'm'), ('Barbe', 'f'),
    ('Barrakuda', 'm'), ('Basilikum', 'n'), ('Baummarder', 'm'), ('Beifuss', 'm'),
    ('Bergamotte', 'f'),
    ('Beutelwolf', 'm'), ('Biber', 'm'), ('Biene', 'f'), ('Bienenfresser', 'm'), ('Birke', 'f'),
    ('Birne', 'f'), ('Bisamratte', 'f'), ('Bison', 'm'), ('Blattlaus', 'f'), ('Blaukraut', 'n'),
    ('Blaumeise', 'f'), ('Blauwal', 'm'), ('Blindschleiche', 'f'), ('Blobfisch', 'm'),
    ('Blumenkohl', 'm'), ('Blutegel', 'm'), ('Bohnenkraut', 'n'), ('Bonobo', 'm'),
    ('Boysenbeere', 'f'),
    ('Brachiosaurus', 'm'), ('Breitmaulnashorn', 'n'), ('Brennnessel', 'f'), ('Brokkoli', 'm'),
    ('Brombeere', 'f'), ('Buchfink', 'm'), ('Buchweizen', 'm'), ('Buckelwal', 'm'),
    ('Buntspecht', 'm'),
    ('Bussard', 'm'), ('Cashewnuss', 'f'), ('Champignon', 'm'), ('Chia', 'f'), ('Chinakohl', 'm'),
    ('Chinchilla', 'n'), ('Clownfisch', 'm'), ('Dachs', 'm'), ('Damhirsch', 'm'), ('Dattel', 'f'),
    ('Delfin', 'm'), ('Dill', 'm'), ('Dingo', 'm'), ('Dinkel', 'm'), ('Diplodokus', 'm'),
    ('Distelfalter', 'm'), ('Dodo', 'm'), ('Dohle', 'f'), ('Dompfaff', 'm'), ('Dorsch', 'm'),
    ('Douglasie', 'f'), ('Drachenfrucht', 'f'), ('Dromedar', 'n'), ('Drossel', 'f'),
    ('Eberesche', 'f'), ('Efeu', 'm'), ('Eibe', 'f'), ('Eiche', 'f'), ('Eidechse', 'f'),
    ('Eintagsfliege', 'f'), ('Eisenhut', 'm'), ('Eisvogel', 'm'), ('Elch', 'm'), ('Elefant', 'm'),
    ('Elster', 'f'), ('Emu', 'm'), ('Ente', 'f'), ('Erdbeere', 'f'), ('Erdferkel', 'n'),
    ('Erle', 'f'), ('Esche', 'f'), ('Esel', 'm'), ('Estragon', 'm'), ('Eule', 'f'),
    ('Eulenfalter', 'm'),
    ('Falke', 'm'), ('Fasan', 'm'), ('Faultier', 'n'), ('Feige', 'f'), ('Feigenbaum', 'm'),
    ('Feldhase', 'm'), ('Feldsalat', 'm'), ('Fenchel', 'm'), ('Fennek', 'm'), ('Feuerqualle', 'f'),
    ('Feuersalamander', 'm'), ('Feuerwanze', 'f'), ('Fichte', 'f'), ('Fingerhut', 'm'),
    ('Fingertier', 'n'), ('Fischotter', 'm'), ('Flamingo', 'm'), ('Fledermaus', 'f'),
    ('Fliege', 'f'), ('Fliegenpilz', 'm'), ('Floh', 'm'), ('Florfliege', 'f'), ('Flughund', 'm'),
    ('Flunder', 'f'), ('Flussbarsch', 'm'), ('Forelle', 'f'), ('Fossa', 'f'), ('Frettchen', 'n'),
    ('Frosch', 'm'), ('Fuchs', 'm'), ('Gans', 'f'), ('Garnele', 'f'), ('Gartenkresse', 'f'),
    ('Gartenkreuzspinne', 'f'), ('Gazelle', 'f'), ('Gecko', 'm'), ('Geier', 'm'), ('Gepard', 'm'),
    ('Gerste', 'f'), ('Gibbon', 'm'), ('Ginkgo', 'm'), ('Ginseng', 'm'), ('Giraffe', 'f'),
    ('Goldammer', 'f'), ('Goldfisch', 'm'), ('Gorilla', 'm'), ('Gottesanbeterin', 'f'),
    ('Granatapfel', 'm'), ('Grapefruit', 'f'), ('Graureiher', 'm'), ('Grottenolm', 'm'),
    ('Gummibaum', 'm'), ('Gurke', 'f'), ('Habicht', 'm'), ('Hafer', 'm'), ('Haflinger', 'm'),
    ('Hagebutte', 'f'), ('Hai', 'm'), ('Hainbuche', 'f'), ('Hallimasch', 'm'),
    ('Halsbandsittich', 'm'),
    ('Hammerhai', 'm'), ('Hamster', 'm'), ('Harpyie', 'f'), ('Hasel', 'f'), ('Haselmaus', 'f'),
    ('Haselnuss', 'f'), ('Hase', 'm'), ('Haubentaucher', 'm'), ('Haussperling', 'm'),
    ('Hecht', 'm'), ('Heidelbeere', 'f'), ('Heimchen', 'n'), ('Herbstzeitlose', 'f'),
    ('Hermelin', 'n'), ('Heuschrecke', 'f'), ('Himbeere', 'f'), ('Hirsch', 'm'), ('Hirse', 'f'),
    ('Holunder', 'm'), ('Honigmelone', 'f'), ('Hopfen', 'm'), ('Hornisse', 'f'), ('Hortensie', 'f'),
    ('Huhn', 'n'), ('Hummer', 'm'), ('Igel', 'm'), ('Iltis', 'm'), ('Impala', 'f'), ('Ingwer', 'm'),
    ('Inlandtaipan', 'm'), ('Islandpferd', 'n'), ('Jaguar', 'm'), ('Johanniskraut', 'n'),
    ('Kabeljau', 'm'), ('Kaiman', 'm'), ('Kaiserpinguin', 'm'), ('Kakadu', 'm'), ('Kaki', 'f'),
    ('Kaktusfeige', 'f'), ('Kamel', 'n'), ('Kamille', 'f'), ('Kanarienvogel', 'm'),
    ('Kaninchen', 'n'),
    ('Kapuzineraffe', 'm'), ('Kapuzinerkresse', 'f'), ('Kardamom', 'm'), ('Karfiol', 'm'),
    ('Karotte', 'f'), ('Karpfen', 'm'), ('Kartoffel', 'f'), ('Kastanie', 'f'), ('Katta', 'f'),
    ('Katze', 'f'), ('Katzenhai', 'm'), ('Kellerassel', 'f'), ('Kichererbse', 'f'),
    ('Kiebitz', 'm'),
    ('Kiefer', 'f'), ('Kirschbaum', 'm'), ('Kiwi', 'f'), ('Kiwi', 'm'), ('Klapperschlange', 'f'),
    ('Kleiber', 'm'), ('Kleidermotte', 'f'), ('Knoblauch', 'm'), ('Knollensellerie', 'm'),
    ('Koala', 'm'), ('Koboldmaki', 'm'), ('Kohl', 'm'), ('Kohlmeise', 'f'), ('Kohlrabi', 'm'),
    ('Kojote', 'm'), ('Kokosnuss', 'f'), ('Kolibri', 'm'), ('Kondor', 'm'), ('Kopfsalat', 'm'),
    ('Koralle', 'f'), ('Koriander', 'm'), ('Kormoran', 'm'), ('Kornnatter', 'f'), ('Krake', 'm'),
    ('Kranich', 'm'), ('Krebs', 'm'), ('Kresse', 'f'), ('Kreuzotter', 'm'), ('Kreuzspinne', 'f'),
    ('Krokodil', 'n'), ('Krokus', 'm'), ('Kuckuck', 'm'), ('Kudu', 'm'), ('Kugelfisch', 'm'),
    ('Kuh', 'f'), ('Lachs', 'm'), ('Lama', 'n'), ('Laubfrosch', 'm'), ('Lauch', 'm'),
    ('Lavendel', 'm'), ('Lebensbaum', 'm'), ('Leguan', 'm'), ('Leistenkrokodil', 'n'),
    ('Lemming', 'm'), ('Lemur', 'm'), ('Leopard', 'm'), ('Lerche', 'f'), ('Leuchtqualle', 'f'),
    ('Libelle', 'f'), ('Liger', 'm'), ('Limette', 'f'), ('Linde', 'f'), ('Litschi', 'f'),
    ('Lorbeerkirsche', 'f'), ('Lorbeer', 'm'), ('Luchs', 'm'), ('Macadamia', 'f'),
    ('Mahagoni', 'n'),
    ('Mais', 'm'), ('Majoran', 'm'), ('Makrele', 'f'), ('Mammutbaum', 'm'), ('Mammut', 'n'),
    ('Mandarine', 'f'), ('Mandrill', 'm'), ('Mangold', 'm'), ('Mango', 'f'), ('Manul', 'm'),
    ('Maracuja', 'f'), ('Marder', 'm'), ('Mauersegler', 'm'), ('Maulbeere', 'f'), ('Maulwurf', 'm'),
    ('Maus', 'f'), ('Mauswiesel', 'n'), ('Meerrettich', 'm'), ('Meerschweinchen', 'n'),
    ('Mehlschwalbe', 'f'), ('Melone', 'f'), ('Miesmuschel', 'f'), ('Milbe', 'f'), ('Minze', 'f'),
    ('Mirabelle', 'f'), ('Mispel', 'f'), ('Mohn', 'm'), ('Molch', 'm'), ('Monarchfalter', 'm'),
    ('Mondfisch', 'm'), ('Morchel', 'f'), ('Mufflon', 'n'), ('Mungo', 'm'), ('Murmeltier', 'n'),
    ('Muskatnuss', 'f'), ('Mutterkorn', 'n'), ('Nachtigall', 'f'), ('Nacktmull', 'm'),
    ('Nandu', 'm'), ('Narwal', 'm'), ('Narzisse', 'f'), ('Nashorn', 'n'), ('Nebelparder', 'm'),
    ('Nektarine', 'f'), ('Nerz', 'm'), ('Neunauge', 'n'), ('Nilpferd', 'n'), ('Nutria', 'f'),
    ('Nymphensittich', 'm'), ('Ohrwurm', 'm'), ('Okapi', 'n'), ('Opossum', 'n'), ('Orange', 'f'),
    ('Orca', 'm'), ('Oregano', 'm'), ('Ozelot', 'm'), ('Pampelmuse', 'f'), ('Panda', 'm'),
    ('Panther', 'm'), ('Papagei', 'm'), ('Papaya', 'f'), ('Pappel', 'f'), ('Paprika', 'm'),
    ('Paradeiser', 'm'), ('Paranuss', 'f'), ('Pavian', 'm'), ('Pekannussbaum', 'm'),
    ('Pelikan', 'm'), ('Perlhuhn', 'n'), ('Perserkatze', 'f'), ('Petersilie', 'f'), ('Pfau', 'm'),
    ('Pfeffer', 'm'), ('Pfefferminze', 'f'), ('Pfeilgiftfrosch', 'm'), ('Pferd', 'n'),
    ('Pfifferling', 'm'), ('Pfirsich', 'm'), ('Pflaume', 'f'), ('Pflaumenbaum', 'm'),
    ('Physalis', 'f'), ('Pinguin', 'm'), ('Pinie', 'f'), ('Piranha', 'm'), ('Pirol', 'm'),
    ('Pistazie', 'f'), ('Platane', 'f'), ('Plesiosaurus', 'm'), ('Polarfuchs', 'm'),
    ('Pomelo', 'f'), ('Porree', 'm'), ('Portulak', 'm'), ('Pottwal', 'm'), ('Preiselbeere', 'f'),
    ('Puma', 'm'), ('Qualle', 'f'), ('Quappe', 'f'), ('Quastenflosser', 'm'), ('Quinoa', 'f'),
    ('Quitte', 'f'), ('Rabe', 'm'), ('Ratte', 'f'), ('Rauchschwalbe', 'f'), ('Rebhuhn', 'n'),
    ('Regenbogenforelle', 'f'), ('Regenwurm', 'm'), ('Reiher', 'm'), ('Reis', 'm'),
    ('Rentier', 'n'),
    ('Rettich', 'm'), ('Rhabarber', 'm'), ('Rhesusaffe', 'm'), ('Rind', 'n'), ('Ringelblume', 'f'),
    ('Ringelnatter', 'f'), ('Robbe', 'f'), ('Robinie', 'f'), ('Rochen', 'm'), ('Roggen', 'm'),
    ('Rosenkohl', 'm'), ('Rosmarin', 'm'), ('Rotbarsch', 'm'), ('Rotbuche', 'f'),
    ('Rotkehlchen', 'n'),
    ('Rotkohl', 'm'), ('Rotkraut', 'n'), ('Rotmilan', 'm'), ('Rucola', 'm'), ('Safran', 'm'),
    ('Salat', 'm'), ('Salbei', 'm'), ('Sardelle', 'f'), ('Sauerampfer', 'm'), ('Schafgarbe', 'f'),
    ('Schaf', 'n'), ('Schakal', 'm'), ('Schimpanse', 'm'), ('Schleie', 'f'), ('Schleiereule', 'f'),
    ('Schlupfwespe', 'f'), ('Schmetterling', 'm'), ('Schnabeltier', 'n'), ('Schnecke', 'f'),
    ('Schneeleopard', 'm'), ('Schnittlauch', 'm'), ('Scholle', 'f'), ('Schwalbe', 'f'),
    ('Schwalbenschwanz', 'm'), ('Schwan', 'm'), ('Schwarzmilan', 'm'), ('Schwarzstorch', 'm'),
    ('Schwarzwurzel', 'f'), ('Schwebfliege', 'f'), ('Schwein', 'n'), ('Schwertfisch', 'm'),
    ('Schwertwal', 'm'), ('Seeadler', 'm'), ('Seegurke', 'f'), ('Seeigel', 'm'), ('Seekuh', 'f'),
    ('Seepferdchen', 'n'), ('Seeschlange', 'f'), ('Sellerie', 'm'), ('Serval', 'm'),
    ('Sesam', 'm'), ('Sharonfrucht', 'f'), ('Shetlandpony', 'n'), ('Shiitake', 'm'),
    ('Siamkatze', 'f'), ('Silberfischchen', 'n'), ('Singdrossel', 'f'), ('Skorpion', 'm'),
    ('Sonnenblume', 'f'), ('Spargel', 'm'), ('Speierling', 'm'), ('Sperling', 'm'), ('Spinat', 'm'),
    ('Spinne', 'f'), ('Spitzkohl', 'm'), ('Spitzwegerich', 'm'), ('Stachelbeere', 'f'),
    ('Stachelschwein', 'n'), ('Stangensellerie', 'm'), ('Star', 'm'), ('Stegosaurus', 'm'),
    ('Steinadler', 'm'), ('Steinbock', 'm'), ('Steinbutt', 'm'), ('Steinkauz', 'm'),
    ('Steinmarder', 'm'), ('Steinpilz', 'm'), ('Sternfrucht', 'f'), ('Stieglitz', 'm'),
    ('Stinktier', 'n'), ('Stockente', 'f'), ('Storch', 'm'), ('Tagpfauenauge', 'n'),
    ('Tanne', 'f'), ('Tapir', 'm'), ('Taube', 'f'), ('Teichmolch', 'm'), ('Termite', 'f'),
    ('Thunfisch', 'm'), ('Thymian', 'm'), ('Tigerhai', 'm'), ('Tiger', 'm'), ('Tintenfisch', 'm'),
    ('Tomate', 'f'), ('Totenkopfaffe', 'm'), ('Trampeltier', 'n'), ('Truthuhn', 'n'),
    ('Tukan', 'm'), ('Tulpe', 'f'), ('Uhu', 'm'), ('Ulme', 'f'), ('Unke', 'f'),
    ('Urzeitkrebs', 'm'),
    ('Vanille', 'f'), ('Veilchen', 'n'), ('Viper', 'f'), ('Vogelspinne', 'f'), ('Wacholder', 'm'),
    ('Wachtel', 'f'), ('Waldkauz', 'm'), ('Waldohreule', 'f'), ('Wallaby', 'n'), ('Wal', 'm'),
    ('Walnuss', 'f'), ('Walross', 'n'), ('Wanderfalke', 'm'), ('Waran', 'm'), ('Wassermelone', 'f'),
    ('Wasserschwein', 'n'), ('Wasserspinne', 'f'), ('Wattwurm', 'm'), ('Weberknecht', 'm'),
    ('Weide', 'f'), ('Weinbergschnecke', 'f'), ('Weisskohl', 'm'), ('Weisskraut', 'n'),
    ('Weizen', 'm'), ('Wellensittich', 'm'), ('Wels', 'm'), ('Wespe', 'f'), ('Wespenspinne', 'f'),
    ('Wiedehopf', 'm'), ('Wildkatze', 'f'), ('Wildschwein', 'n'), ('Winkelspinne', 'f'),
    ('Wirsing', 'm'), ('Wisent', 'm'), ('Wolf', 'm'), ('Wombat', 'm'), ('Yak', 'm'),
    ('Zander', 'm'), ('Zauneidechse', 'f'), ('Zebrafink', 'm'), ('Zebra', 'n'), ('Zecke', 'f'),
    ('Zeder', 'f'), ('Ziege', 'f'), ('Ziesel', 'm'), ('Zikade', 'f'), ('Zilpzalp', 'm'),
    ('Zimt', 'm'), ('Zitrone', 'f'), ('Zitronenfalter', 'm'), ('Zitronenmelisse', 'f'),
    ('Zitteraal', 'm'), ('Zitterspinne', 'f'), ('Zucchini', 'f'), ('Zuckermais', 'm'),
    ('Zwetschge', 'f'), ('Zwiebel', 'f'), ('Zypresse', 'f')
]

adjs = {"m": [
    'absoluter', 'adretter', 'agiler', 'akkurater', 'aktiver', 'aktueller', 'angenehmer',
    'anteiliger', 'artiger', 'aufrechter', 'autonomer', 'begehrter', 'behutsamer', 'bejubelter',
    'bekannter', 'beliebter', 'bequemer', 'bereiter', 'besonderer', 'besonnener', 'besserer',
    'bewegender', 'blendender', 'bombiger', 'brandneuer', 'brillanter', 'bunter', 'charmanter',
    'cleverer', 'cooler', 'dankbarer', 'dienlicher', 'diskreter', 'edler', 'effektiver',
    'ehrlicher', 'eifriger', 'einfacher', 'einmaliger', 'eleganter', 'enormer', 'epochaler',
    'erfahrener', 'ergiebiger', 'erhebender', 'erholsamer', 'exakter', 'exklusiver',
    'exotischer', 'explosiver', 'exquisiter', 'fairer', 'famoser', 'feiner', 'fertiger',
    'fescher', 'fesselnder', 'festlicher', 'fideler', 'findiger', 'fitter', 'flexibler',
    'flinker', 'flotter', 'freier', 'freudiger', 'froher', 'galanter', 'gediegener',
    'geduldiger', 'geeigneter', 'gefeierter', 'gefragter', 'gehorsamer', 'gelassener',
    'geliebter', 'gelungener', 'genauer', 'genehmer', 'genialer', 'geordneter', 'gepflegter',
    'gerechter', 'geruhsamer', 'gesunder', 'getreuer', 'gewaltiger', 'gezielter', 'glasklarer',
    'glatter', 'glorioser', 'goldener', 'goldiger', 'grandioser', 'greifbarer', 'guter',
    'handfester', 'handlicher', 'heiler', 'heiliger', 'heilsamer', 'heiterer', 'heller',
    'herrlicher', 'herziger', 'herzlicher', 'hoher', 'humaner', 'idealer', 'illustrer',
    'immenser', 'imposanter', 'intakter', 'integrer', 'intensiver', 'klagloser', 'klarer',
    'kluger', 'knuffiger', 'kommoder', 'kompletter', 'konkreter', 'konstanter', 'korrekter',
    'kostbarer', 'kreativer', 'kritischer', 'kulanter', 'lebendiger', 'lebhafter', 'legaler',
    'legitimer', 'leichter', 'liberaler', 'lieber', 'lockerer', 'logischer', 'lohnender',
    'loyaler', 'lukrativer', 'magischer', 'makelloser', 'markanter', 'massiver', 'maximaler',
    'messbarer', 'milder', 'mobiler', 'moderner', 'mutiger', 'naher', 'namhafter', 'netter',
    'neuer', 'niedlicher', 'optimaler', 'originaler', 'packender', 'passender', 'perfekter',
    'planvoller', 'plausibler', 'positiver', 'potenter', 'praller', 'protziger', 'puppiger',
    'rationaler', 'reicher', 'reifer', 'reiner', 'reizender', 'reizvoller', 'relevanter',
    'rentabler', 'richtiger', 'riesiger', 'robuster', 'rosaroter', 'rosiger', 'ruhiger',
    'sanfter', 'satter', 'sauberer', 'scharfer', 'schicker', 'schlanker', 'schlauer',
    'schmucker', 'schneller', 'sensibler', 'sicherer', 'sichtbarer', 'simpler', 'sinnvoller',
    'solider', 'sonniger', 'sorgloser', 'sorgsamer', 'spannender', 'sparsamer', 'spezieller',
    'spielender', 'stabiler', 'starker', 'steigender', 'stilvoller', 'stolzer', 'tadelloser',
    'tauglicher', 'tierischer', 'toleranter', 'toller', 'treffender', 'treuer', 'umjubelter',
    'ungeahnter', 'verdienter', 'verehrter', 'veritabler', 'vermehrter', 'versierter',
    'vertrauter', 'vitaler', 'wachsamer', 'wachsender', 'wahrer', 'warmer', 'weicher',
    'weiser', 'wertiger', 'wertvoller', 'wichtiger', 'wirksamer', 'witziger', 'wohliger',
    'wohnlicher'
], "f": [
    'absolute', 'adrette', 'agile', 'akkurate', 'aktive', 'aktuelle', 'akzeptable', 'allerbeste',
    'allererste', 'anerkannte', 'angenehme', 'angesehene', 'annehmbare', 'anteilige',
    'artige', 'attraktive', 'aufrechte', 'aufwendige', 'autonome', 'bedeutende', 'bedeutsame',
    'begehrte', 'behagliche', 'beheizbare', 'behutsame', 'bejubelte', 'bekannte', 'bekennende',
    'belastbare', 'belehrbare', 'beliebte', 'bequeme', 'bereite', 'besondere', 'besonnene',
    'bessere', 'bevorzugte', 'bewegende', 'bewunderte', 'blendende', 'bombige', 'brandneue',
    'brillante', 'bunte', 'charmante', 'clevere', 'coole', 'dankbare', 'dauerhafte',
    'dienliche', 'diskrete', 'dynamische', 'edle', 'effektive', 'effiziente', 'ehrenwerte',
    'ehrgeizige', 'ehrliche', 'eifrige', 'eindeutige', 'einfache', 'einmalige', 'elegante',
    'energische', 'enorme', 'epochale', 'erfahrene', 'ergiebige', 'erhebende', 'erhebliche',
    'erholsame', 'erkennbare', 'ernsthafte', 'erweiterte', 'etablierte', 'exakte', 'exklusive',
    'exotische', 'explosive', 'exquisite', 'exzellente', 'fabelhafte', 'faire', 'famose',
    'feine', 'fertige', 'fesche', 'fesselnde', 'festliche', 'fidele', 'findige', 'fitte',
    'flexible', 'flinke', 'flotte', 'freie', 'freudige', 'friedliche', 'friedvolle',
    'frohe', 'fruchtbare', 'fulminante', 'furchtlose', 'galante', 'gediegene', 'geduldige',
    'geeignete', 'gefeierte', 'gefesselte', 'gefestigte', 'gefragte', 'gehorsame', 'gelassene',
    'geliebte', 'gelungene', 'gemeinsame', 'genaue', 'genehme', 'geniale', 'geordnete',
    'gepflegte', 'gerechte', 'geruhsame', 'geschickte', 'gestiegene', 'gesunde', 'getreue',
    'gewachsene', 'gewaltige', 'gewichtige', 'gezielte', 'glanzvolle', 'glasklare', 'glatte',
    'gloriose', 'glorreiche', 'goldene', 'goldige', 'grandiose', 'greifbare', 'gute',
    'gutgehende', 'handfeste', 'handliche', 'heile', 'heilige', 'heilsame', 'heitere',
    'helle', 'herrliche', 'herzige', 'herzliche', 'hilfreiche', 'himmlische', 'hohe',
    'humane', 'humorvolle', 'ideale', 'idyllische', 'illustre', 'immense', 'imposante',
    'innovative', 'intakte', 'integre', 'intensive', 'klaglose', 'klare', 'klassische',
    'kluge', 'knuddelige', 'knuffige', 'kollegiale', 'kommode', 'kompatible', 'kompetente',
    'komplette', 'kongeniale', 'konkrete', 'konstante', 'korrekte', 'kostbare', 'kostenlose',
    'kraftvolle', 'kreative', 'kritische', 'kulante', 'kunstvolle', 'langlebige', 'lautstarke',
    'lebendige', 'lebhafte', 'legale', 'legitime', 'leichte', 'leuchtende', 'leutselige',
    'liberale', 'liebe', 'liebevolle', 'lockere', 'logische', 'lohnende', 'loyale', 'lukrative',
    'magische', 'makellose', 'malerische', 'markante', 'massive', 'maximale', 'messbare',
    'milde', 'mobile', 'moderne', 'moralische', 'motivierte', 'mutige', 'nahe', 'namhafte',
    'nette', 'neue', 'niedliche', 'optimale', 'originale', 'packende', 'passende', 'perfekte',
    'planvolle', 'plausible', 'positive', 'potente', 'praktische', 'pralle', 'produktive',
    'profitable', 'prominente', 'protzige', 'prunkvolle', 'puppige', 'rationale', 'rechtliche',
    'reiche', 'reife', 'reine', 'reizende', 'reizvolle', 'relevante', 'rentable', 'richtige',
    'riesige', 'robuste', 'rosarote', 'rosige', 'ruhige', 'ruhmreiche', 'sagenhafte',
    'sanfte', 'satte', 'saubere', 'scharfe', 'schicke', 'schlagende', 'schlanke', 'schlaue',
    'schmucke', 'schnelle', 'schuldlose', 'sensible', 'sichere', 'sichtbare', 'simple',
    'sinnvolle', 'solide', 'sonnige', 'sorglose', 'sorgsame', 'spannende', 'sparsame',
    'spezielle', 'spielende', 'stabile', 'standhafte', 'starke', 'stattliche', 'steigende',
    'stilvolle', 'stolze', 'strahlende', 'tadellose', 'taugliche', 'tierische', 'tolerante',
    'tolle', 'traumhafte', 'treffende', 'treffliche', 'treue', 'triumphale', 'ultimative',
    'umfassende', 'umjubelte', 'umsichtige', 'umwerfende', 'unbedingte', 'unfehlbare',
    'ungeahnte', 'ungeteilte', 'verdiente', 'verehrte', 'veritable', 'vermehrte', 'versierte',
    'vertraute', 'vitale', 'wachsame', 'wachsende', 'wahre', 'warme', 'weiche', 'weise',
    'wertige', 'wertvolle', 'wichtige', 'wirksame', 'witzige', 'wohlige', 'wohltuende',
    'wohnliche', 'wunderbare', 'wundersame', 'zufriedene'
], "n": [
    'absolutes', 'adrettes', 'agiles', 'akkurates', 'aktives', 'aktuelles', 'angenehmes',
    'anteiliges', 'artiges', 'aufrechtes', 'autonomes', 'begehrtes', 'behutsames', 'bejubeltes',
    'bekanntes', 'beliebtes', 'bequemes', 'bereites', 'besonderes', 'besonnenes', 'besseres',
    'bewegendes', 'blendendes', 'bombiges', 'brandneues', 'brillantes', 'buntes', 'charmantes',
    'cleveres', 'cooles', 'dankbares', 'dienliches', 'diskretes', 'edles', 'effektives',
    'ehrliches', 'eifriges', 'einfaches', 'einmaliges', 'elegantes', 'enormes', 'epochales',
    'erfahrenes', 'ergiebiges', 'erhebendes', 'erholsames', 'exaktes', 'exklusives',
    'exotisches', 'explosives', 'exquisites', 'faires', 'famoses', 'feines', 'fertiges',
    'fesches', 'fesselndes', 'festliches', 'fideles', 'findiges', 'fittes', 'flexibles',
    'flinkes', 'flottes', 'freies', 'freudiges', 'frohes', 'galantes', 'gediegenes',
    'geduldiges', 'geeignetes', 'gefeiertes', 'gefragtes', 'gehorsames', 'gelassenes',
    'geliebtes', 'gelungenes', 'genaues', 'genehmes', 'geniales', 'geordnetes', 'gepflegtes',
    'gerechtes', 'geruhsames', 'gesundes', 'getreues', 'gewaltiges', 'gezieltes', 'glasklares',
    'glattes', 'glorioses', 'goldenes', 'goldiges', 'grandioses', 'greifbares', 'gutes',
    'handfestes', 'handliches', 'heiles', 'heiliges', 'heilsames', 'heiteres', 'helles',
    'herrliches', 'herziges', 'herzliches', 'hohes', 'humanes', 'ideales', 'illustres',
    'immenses', 'imposantes', 'intaktes', 'integres', 'intensives', 'klagloses', 'klares',
    'kluges', 'knuffiges', 'kommodes', 'komplettes', 'konkretes', 'konstantes', 'korrektes',
    'kostbares', 'kreatives', 'kritisches', 'kulantes', 'lebendiges', 'lebhaftes', 'legales',
    'legitimes', 'leichtes', 'liberales', 'liebes', 'lockeres', 'logisches', 'lohnendes',
    'loyales', 'lukratives', 'magisches', 'makelloses', 'markantes', 'massives', 'maximales',
    'messbares', 'mildes', 'mobiles', 'modernes', 'mutiges', 'nahes', 'namhaftes', 'nettes',
    'neues', 'niedliches', 'optimales', 'originales', 'packendes', 'passendes', 'perfektes',
    'planvolles', 'plausibles', 'positives', 'potentes', 'pralles', 'protziges', 'puppiges',
    'rationales', 'reiches', 'reifes', 'reines', 'reizendes', 'reizvolles', 'relevantes',
    'rentables', 'richtiges', 'riesiges', 'robustes', 'rosarotes', 'rosiges', 'ruhiges',
    'sanftes', 'sattes', 'sauberes', 'scharfes', 'schickes', 'schlankes', 'schlaues',
    'schmuckes', 'schnelles', 'sensibles', 'sicheres', 'sichtbares', 'simples', 'sinnvolles',
    'solides', 'sonniges', 'sorgloses', 'sorgsames', 'spannendes', 'sparsames', 'spezielles',
    'spielendes', 'stabiles', 'starkes', 'steigendes', 'stilvolles', 'stolzes', 'tadelloses',
    'taugliches', 'tierisches', 'tolerantes', 'tolles', 'treffendes', 'treues', 'umjubeltes',
    'ungeahntes', 'verdientes', 'verehrtes', 'veritables', 'vermehrtes', 'versiertes',
    'vertrautes', 'vitales', 'wachsames', 'wachsendes', 'wahres', 'warmes', 'weiches',
    'weises', 'wertiges', 'wertvolles', 'wichtiges', 'wirksames', 'witziges', 'wohliges',
    'wohnliches'
]}


def generate_name_de(length=15):
    while True:
        noun, gender = random.choice(nouns)
        adj = random.choice(adjs[gender])
        name = adj[:1].upper() + adj[1:] + noun
        if len(name) <= length:
            return name


if __name__ == "__main__":
    for i in range(100):
        print(generate_name_de())
