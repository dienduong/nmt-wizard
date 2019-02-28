# -*- coding: utf-8 -*

import random
import re

# True if masculine, form
nouns = [
    (True, "abyssin", "bunny cat"),
    (True, "accenteur", "prunella"),
    (True, "addax", "addax"),
    (True, "agouti", "agouti"),
    (True, "aigle", "eagle"),
    (True, "alligator", "alligator"),
    (True, "alpaga", "alpaca"),
    (True, "anhinga", "anhinga"),
    (False, "antilope", "antelope"),
    (True, "appaloosa", "appaloosa"),
    (True, "ara", "macaw"),
    (True, "argus", "argus"),
    (True, "atèle", "spider monkey"),
    (True, "aubrac", "aubrac"),
    (True, "axolotl", "axolotl"),
    (True, "babiroussa", "babirusa"),
    (True, "babouin", "baboon"),
    (True, "bandicoot", "bandicoot"),
    (True, "barbican", "barbican"),
    (True, "baribal", "black bear"),
    (True, "barzoï", "Borzoi"),
    (True, "basilic", "basilisk"),
    (True, "bateleur", "bateleur"),
    (True, "baudet", "donkey"),
    (True, "bihoreau", "night heron"),
    (True, "binturong", "binturong"),
    (True, "bison", "buffalo"),
    (True, "blaireau", "badger"),
    (True, "boeuf", "oxen"),
    (True, "boto", "boto"),
    (True, "bouledogue", "bulldog"),
    (True, "bouquetin", "ibex"),
    (True, "bourdon", "bumblebee"),
    (True, "bouvier", "cattle dog"),
    (True, "boxer", "boxer"),
    (True, "brochet", "pike"),
    (True, "bubale", "hartebeest"),
    (True, "buffle", "buffalo"),
    (True, "butor", "bittern"),
    (True, "cacatoès", "cockatoo"),
    (True, "cachalot", "sperm whale"),
    (True, "calao", "hornbill"),
    (True, "camargue", "camargue horse"),
    (True, "campagnol", "vole"),
    (True, "caméléon", "chameleon"),
    (True, "canard", "duck"),
    (True, "capucin", "capuchin"),
    (True, "capybara", "capybara"),
    (True, "caracal", "caracal"),
    (True, "carcajou", "glutton"),
    (True, "caribou", "caribou"),
    (True, "casoar", "cassowary"),
    (True, "castor", "beaver"),
    (True, "caïman", "caiman"),
    (True, "cerf", "stag"),
    (True, "chacal", "jackal"),
    (True, "chameau", "camel"),
    (True, "chamois", "chamois"),
    (True, "chardonneret", "goldfinch"),
    (True, "chat", "cat"),
    (True, "cheval", "horse"),
    (True, "chevreuil", "roe deer"),
    (True, "chevrotin", "chevrotin"),
    (True, "chien", "dog"),
    (True, "chimpanzé", "chimpanzee"),
    (True, "colibri", "hummingbird"),
    (True, "colley", "collie"),
    (True, "condor", "condor"),
    (True, "coq", "rooster"),
    (True, "coque", "shell"),
    (True, "corbeau", "raven"),
    (True, "cormoran", "cormorant"),
    (True, "coucou", "cuckoo"),
    (True, "coyote", "coyote"),
    (True, "crapaud", "toad"),
    (True, "crevette", "shrimp"),
    (True, "crocodile", "crocodile"),
    (True, "cygne", "swan"),
    (True, "daim", "fallow deer"),
    (True, "dalmatien", "dalmatian"),
    (True, "daman", "dassie"),
    (True, "dauphin", "dolphin"),
    (True, "dindon", "turkey"),
    (True, "dingo", "dingo"),
    (True, "dodo", "dodo"),
    (True, "dogue", "dogo"),
    (True, "doryphore", "Colorado beetle"),
    (True, "douc", "douc"),
    (True, "dragon", "dragon"),
    (True, "dromadaire", "camel"),
    (True, "ecureuil", "squirrel"),
    (True, "eider", "eider"),
    (True, "elan", "elk"),
    (True, "elephant", "elephant"),
    (True, "emeu", "emu"),
    (True, "entelle", "langur monkey"),
    (True, "escargot", "snail"),
    (True, "etourneau", "starling"),
    (True, "faisan", "pheasant"),
    (True, "faucon", "falcon"),
    (True, "fennec", "fennec"),
    (True, "flamant-rose", "flamingo"),
    (True, "frelon", "hornet"),
    (True, "frison", "Friesian horse"),
    (True, "gavial", "gharial"),
    (True, "geai", "jay"),
    (True, "gecko", "gecko"),
    (True, "gerenuk", "gerenuk"),
    (True, "gibbon", "gibbon"),
    (True, "glouton", "glutton"),
    (True, "gnou", "wildebeest"),
    (True, "gorille", "gorilla"),
    (True, "goujon", "gudgeon"),
    (True, "goéland", "gull"),
    (True, "grillon", "cricket"),
    (True, "guanaco", "guanaco"),
    (True, "guépard", "cheetah"),
    (True, "haflinger", "haflinger"),
    (True, "hamster", "hamster"),
    (True, "harfang", "snowy owl"),
    (True, "henson", "henson horse"),
    (True, "hippopotame", "hippopotamus"),
    (True, "hoazin", "hoatzin"),
    (False, "hyène", "hyena"),
    (True, "hérisson", "hedgehog"),
    (True, "héron", "heron"),
    (True, "ibijau", "potoo"),
    (True, "ibis", "ibis"),
    (True, "iguane", "iguana"),
    (True, "impala", "impala"),
    (True, "indri", "indri"),
    (True, "jabiru", "jabiru"),
    (True, "jacamar", "jacamar"),
    (True, "jaguar", "jaguar"),
    (True, "jaguarondi", "jaguarundi"),
    (True, "kangourou", "kangaroo"),
    (True, "kakapo", "owl parrot"),
    (True, "kiwi", "kiwi"),
    (True, "koala", "koala"),
    (True, "lagopède", "lagopus"),
    (True, "lama", "llama"),
    (True, "lamantin", "manatee"),
    (True, "langur", "langur"),
    (True, "lapin", "rabbit"),
    (True, "lion", "lion"),
    (True, "lipizzan", "lipizzan"),
    (True, "lièvre", "hare"),
    (True, "loir", "dormouse"),
    (True, "loriquet", "loriquet"),
    (True, "loup", "wolf"),
    (True, "lucane", "lucanum"),
    (True, "lycaon", "wild dog"),
    (True, "lynx", "lynx"),
    (True, "léopard", "leopard"),
    (True, "lérot", "garden dormouse"),
    (True, "lézard", "lizard"),
    (True, "macaque", "macaque"),
    (True, "macareux", "puffin"),
    (True, "machaon", "machaon"),
    (True, "maki", "maki"),
    (True, "mammouth", "mammoth"),
    (True, "manchot", "penguin"),
    (True, "mandrill", "mandrill"),
    (True, "manul", "manul"),
    (True, "mara", "patagonian mara"),
    (True, "marabout", "leptoptilos"),
    (True, "margay", "margay"),
    (True, "markhor", "markhor"),
    (True, "merle", "blackbird"),
    (True, "milan", "kite"),
    (True, "moloch", "muloch"),
    (True, "monarque", "monarch"),
    (True, "morse", "walrus"),
    (True, "motmot", "motmot"),
    (True, "mouflon", "mouflon"),
    (True, "mouton", "sheep"),
    (True, "mulot", "field mouse"),
    (True, "muntjac", "muntjac"),
    (True, "muscardin", "hazel dormouse"),
    (True, "myrmidon", "antwren"),
    (True, "narval", "narwhal"),
    (True, "nasique", "long-nosed monkey"),
    (True, "numbat", "numbat"),
    (True, "nyala", "nyala"),
    (True, "ocelot", "ocelot"),
    (True, "okapi", "okapi"),
    (True, "olinguito", "olinguito"),
    (True, "opossum", "opossum"),
    (True, "orang-outan", "orangutan"),
    (True, "orignal", "moose"),
    (True, "ornithorynque", "platypus"),
    (True, "orque", "killer whale"),
    (True, "orvet", "slow worm"),
    (True, "oryctérope", "aardvark"),
    (True, "oryx", "oryx"),
    (True, "otocyon", "otocyon"),
    (True, "ouakari", "ouakari"),
    (True, "ouandérou", "ouandérou"),
    (True, "ouaouaron", "bullfrog"),
    (True, "ouistiti", "marmoset"),
    (True, "ours", "bear"),
    (True, "panda", "panda"),
    (True, "pangolin", "pangolin"),
    (True, "paon", "peacock"),
    (True, "paresseux", "sloth"),
    (True, "percheron", "percheron horse"),
    (True, "phasme", "phasmatodea"),
    (True, "phoque", "seal"),
    (True, "picvert", "woodpecker"),
    (True, "pinson", "finch"),
    (True, "pièride", "pieridae"),
    (True, "poisson", "fish"),
    (True, "porc", "pork"),
    (True, "porcepic", "porcupine"),
    (True, "puma", "puma"),
    (True, "putois", "polecat"),
    (True, "pygargue", "sea eagle"),
    (True, "pécari", "peccary"),
    (True, "pélican", "pelican"),
    (True, "ragondin", "coypu"),
    (True, "raton", "raccoon"),
    (True, "renard", "fox"),
    (True, "renne", "reindeer"),
    (True, "requin", "shark"),
    (True, "rhinocéros", "rhinoceros"),
    (True, "saki", "saki"),
    (True, "samoyède", "samoyed dog"),
    (True, "sanglier", "boar"),
    (True, "serpentaire", "serpent eagle"),
    (True, "serval", "serval"),
    (True, "siamois", "siamese"),
    (True, "silure", "catfish"),
    (True, "singe", "monkey"),
    (True, "sizerin", "redpoll"),
    (True, "smilodon", "smilodon"),
    (True, "sphynx", "sphynx"),
    (True, "springbok", "springbok"),
    (True, "steenbok", "steenbok"),
    (True, "suricate", "meerkat"),
    (True, "takin", "takin"),
    (True, "tamandua", "tamandua"),
    (True, "tamanoir", "giant anteater"),
    (True, "tamarin", "tamarin"),
    (True, "tantale", "mycteria"),
    (True, "tapir", "tapir"),
    (True, "tarier", "saxicola"),
    (True, "tarsier", "tarsier"),
    (True, "tatou", "armadillo"),
    (True, "tchitrec", "tchitrec"),
    (True, "tenrec", "tenrec"),
    (True, "thon", "tuna fish"),
    (True, "tigre", "tiger"),
    (True, "tisserin", "weaver"),
    (True, "topi", "topi"),
    (True, "toucan", "toucan"),
    (True, "touraco", "touraco"),
    (True, "triton", "newt"),
    (True, "trogon", "trogon"),
    (True, "tyrannosaure", "tyrannosaurus"),
    (True, "tétras", "grouse"),
    (True, "unau", "two-toed sloth"),
    (True, "varan", "monitor lizard"),
    (True, "vautour", "vulture"),
    (True, "ver", "worm"),
    (True, "viscache", "viscose"),
    (True, "vison", "mink"),
    (True, "wallaby", "wallaby"),
    (True, "wapiti", "elk"),
    (True, "wombat", "wombat"),
    (True, "xylocope", "xylocope"),
    (True, "yack", "yak"),
    (True, "yapock", "yapock"),
    (True, "yorkshire", "yorkshire"),
    (True, "zèbre", "zebra"),
    (False, "abeille", "bee"),
    (False, "aigrette", "egret"),
    (False, "alouette", "lark"),
    (False, "argiope", "argiope"),
    (False, "autruche", "ostrich"),
    (False, "baleine", "whale"),
    (False, "belette", "weasel"),
    (False, "bergeronnette", "wagtail"),
    (False, "bernache", "black geese"),
    (False, "buse", "buzzard"),
    (False, "béluga", "beluga whale"),
    (False, "caille", "quail"),
    (False, "chauve-souris", "bat"),
    (False, "chouette", "owl"),
    (False, "chèvre", "goat"),
    (False, "cigale", "cicada"),
    (False, "cigogne", "stork"),
    (False, "circaète", "snake eagle"),
    (False, "civette", "civet"),
    (False, "coccinelle", "ladybug"),
    (False, "corneille", "crow"),
    (False, "couleuvre", "snake"),
    (False, "cétoine", "beetle"),
    (False, "dasyure", "quoll"),
    (False, "échasse", "stilt"),
    (False, "fauvette", "warbler"),
    (False, "fouine", "weasel"),
    (False, "fourmi", "ant"),
    (False, "gazelle", "gazelle"),
    (False, "genette", "genet"),
    (False, "girafe", "giraffe"),
    (False, "grenouille", "frog"),
    (False, "grue", "crane"),
    (False, "guêpe", "wasp"),
    (False, "gypaète", "vulture"),
    (False, "harpie", "harpy"),
    (False, "hermine", "ermine"),
    (False, "hirondelle", "swallow"),
    (False, "huitre", "oyster"),
    (False, "hydropote", "hydropot"),
    (False, "jument", "mare"),
    (False, "libellule", "dragonfly"),
    (False, "linotte", "linnet"),
    (False, "loutre", "otter"),
    (False, "malamute", "malamute"),
    (False, "mamba", "mamba"),
    (False, "mangouste", "mongoose"),
    (False, "mante", "mantis"),
    (False, "marmotte", "groundhog"),
    (False, "martre", "marten"),
    (False, "morue", "codfish"),
    (False, "mouche", "fly"),
    (False, "moucherolle", "flycatcher"),
    (False, "mouffette", "skunk"),
    (False, "moule", "mussel"),
    (False, "musaraigne", "shrew"),
    (False, "mésange", "titmouse"),
    (False, "nyctale", "boreal owl"),
    (False, "ombrette", "hamerkop"),
    (False, "oriole", "oriole"),
    (False, "otarie", "sea lion"),
    (False, "pacarana", "pacarana"),
    (False, "panthère", "panther"),
    (False, "panure", "bearded reedling"),
    (False, "paruline", "warbler"),
    (False, "perche", "perch"),
    (False, "perruche", "parakeet"),
    (True, "pétrogale", "rock wallaby"),
    (False, "phacochère", "warthog"),
    (False, "pie", "magpie"),
    (False, "pintade", "guinea fowl"),
    (False, "pirolle", "pirolle"),
    (False, "potamochère", "bushpig"),
    (False, "poule", "hen"),
    (False, "quokka", "quokka"),
    (False, "raie", "ray fish"),
    (False, "rouge-gorge", "robin"),
    (False, "rouge-queue", "redstart"),
    (False, "salamandre", "salamander"),
    (False, "sauterelle", "grasshopper"),
    (False, "sittelle", "nuthatch"),
    (False, "souris", "mouse"),
    (False, "spizaète", "spizate"),
    (False, "tamia", "chipmunk"),
    (False, "tanche", "tench"),
    (False, "tarentaise", "tarentaise"),
    (False, "tarine", "tarine"),
    (False, "taupe", "mole"),
    (False, "tortue", "turtle"),
    (False, "truite", "trout"),
    (False, "vigogne", "vicuña"),
    (False, "vipère", "viper"),
    (False, "viscache", "vizcachas")
]

adjs = [
    (False, "accueillant", "accueillante", "welcoming"),
    (False, "adorable", "adorable", "adorable"),
    (False, "alourdi", "alourdie", "weighed down"),
    (False, "attifé", "attifée", "rigged out"),
    (False, "attrayant", "attrayante", "attractive"),
    (True, "beau/bel", "belle", "beautiful"),
    (False, "carré", "carrée", "square"),
    (False, "confiant", "confiante", "confident"),
    (False, "costaud", "costaude", "hefty"),
    (False, "crasseux", "crasseuse", "filthy"),
    (False, "désillusionné", "désillusionnée", "disillusioned"),
    (False, "dynamique", "dynamique", "dynamic"),
    (False, "élégant", "élégante", "elegant"),
    (False, "élevé", "élevée", "high"),
    (False, "énervé", "énervée", "angry"),
    (False, "gai", "gaie", "cheerful"),
    (True, "gentil", "gentille", "kind"),
    (True, "gros", "grosse", "big"),
    (False, "habillé", "habillée", "dressed up"),
    (False, "hideux", "hideuse", "hideous"),
    (False, "hirsute", "hirsute", "shaggy"),
    (False, "inquiet", "inquiète", "worried"),
    (False, "magnifique", "magnifique", "stunning"),
    (True, "maigre", "maigre", "thin"),
    (False, "maladroit", "maladroite", "clumsy"),
    (False, "merveilleux", "merveilleuse", "marvelous"),
    (False, "mince", "mince", "slender"),
    (False, "nerveux", "nerveuse", "nervous"),
    (False, "offensé", "offensée", "offended"),
    (False, "parfait", "parfaite", "perfect"),
    (False, "plaisant", "plaisante", "pleasant"),
    (False, "propre", "propre", "specific"),
    (False, "impeccable", "impeccable", "impeccable"),
    (False, "méticuleux", "méticuleux", "meticulous"),
    (False, "pimpant", "pimpante", "dashing"),
    (False, "raffiné", "raffinée", "sophisticated"),
    (False, "présentable", "présentable", "presentable"),
    (False, "soigneux", "soigneuse", "careful"),
    (False, "chic", "chic", "chic"),
    (False, "convenable", "convenable", "suitable"),
    (False, "ravissant", "ravissante", "beautiful"),
    (False, "réfléchi", "réfléchie", "deliberate"),
    (False, "sale", "sale", "dirty"),
    (False, "sauvage", "sauvage", "savage"),
    (False, "séduisant", "séduisante", "attractive"),
    (False, "snob", "snob", "snobbish"),
    (False, "sombre", "sombre", "gloomy"),
    (False, "souriant", "souriante", "smiling"),
    (False, "splendide", "splendide", "splendid"),
    (False, "svelte", "svelte", "slender"),
    (False, "tendu", "tendue", "tense"),
    (False, "terne", "terne", "dull"),
    (False, "timide", "timide", "shy"),
    (False, "trompeur", "trompeuse", "misleading"),
    (False, "vif", "vive", "vivid"),
    (False, "vivace", "vivace", "perennial"),
    (False, "agressif", "agressive", "aggressive"),
    (False, "ambitieux", "ambitieuse", "ambitious"),
    (False, "amusant", "amusante", "fun"),
    (False, "amusé", "amusée", "amused"),
    (False, "avare", "avare", "miserly"),
    (False, "brave", "brave", "brave"),
    (False, "brillant", "brillante", "shiny"),
    (False, "chaleureux", "chaleureuse", "warm"),
    (False, "combatif", "combative", "competitive"),
    (False, "coopératif", "coopérative", "cooperative"),
    (False, "cruel", "cruelle", "cruel"),
    (False, "dangereux", "dangereuse", "dangerous"),
    (False, "désagréable", "désagréable", "unpleasant"),
    (False, "déterminé", "déterminée", "specific"),
    (False, "diligent", "diligente", "diligent"),
    (False, "dominant", "dominante", "dominant"),
    (False, "doué", "douée", "talented"),
    (False, "égoïste", "égoïste", "selfish"),
    (False, "entraînant", "entraînante", "catchy"),
    (False, "farfelu", "farfelue", "strange"),
    (False, "fatigant", "fatigante", "tedious"),
    (False, "franc", "franche", "straightforward"),
    (False, "généreux", "généreuse", "generous"),
    (False, "harmonieux", "harmonieuse", "harmonious"),
    (False, "hésitant", "hésitante", "hesitant"),
    (False, "impartial", "impartiale", "impartial"),
    (False, "informé", "informée", "informed"),
    (False, "instinctif", "instinctive", "instinctive"),
    (False, "intrépide", "intrépide", "intrepid"),
    (False, "succinct", "succincte", "brief"),
    (False, "bref", "brève", "brief"),
    (False, "véloce", "véloce", "swift"),
    (False, "fugitif", "fugitive", "fugitive"),
    (False, "furtif", "furtive", "sneaky"),
    (False, "ailé", "ailée", "winged"),
    (False, "poilu", "poilue", "hairy"),
    (False, "chauve", "chauve", "bald"),
    (False, "imberbe", "imberbe", "hairless"),
    (False, "courageux", "courageuse", "brave"),
    (False, "jaloux", "jalouse", "jealous"),
    (False, "lâche", "lâche", "coward"),
    (False, "loufoque", "loufoque", "crazy"),
    (False, "mystérieux", "mystérieuse", "mysterious"),
    (False, "placide", "placide", "staid"),
    (False, "ponctuel", "ponctuelle", "one-time"),
    (False, "posé", "posée", "calm"),
    (False, "protecteur", "protecteure", "protective"),
    (False, "regardant", "regardante", "observant"),
    (False, "sage", "sage", "wise"),
    (False, "scélérat", "scélérate", "villainous"),
    (False, "serviable", "serviable", "helpful"),
    (False, "sincère", "sincère", "sincere"),
    (False, "talentueux", "talentueuse", "talented"),
    (False, "truculent", "truculente", "truculent"),
    (False, "vorace", "vorace", "voracious"),
    (False, "amoureux", "amoureuse", "amorous"),
    (False, "anxieux", "anxieuse", "anxious"),
    (True, "beau", "belle", "beautiful"),
    (False, "bourru", "bourrue", "gruff"),
    (False, "calme", "calme", "calm"),
    (False, "choqué", "choquée", "shocked"),
    (False, "coquin", "coquine", "naughty"),
    (False, "coupable", "coupable", "guilty"),
    (False, "débordé", "débordée", "overflowing"),
    (False, "dégoûté", "dégoûtée", "disgusted"),
    (False, "déprimé", "déprimée", "depressed"),
    (False, "dérangé", "dérangée", "disturbed"),
    (False, "douloureux", "douloureuse", "painful"),
    (False, "effrayé", "effrayée", "scared"),
    (False, "ennuyé", "ennuyée", "annoyed"),
    (False, "envieux", "envieuse", "envious"),
    (False, "épuisé", "épuisée", "exhausted"),
    (False, "exaspéré", "exaspérée", "infuriated"),
    (False, "extatique", "extatique", "ecstatic"),
    (False, "fâché", "fâchée", "angry"),
    (False, "fatigué", "fatiguée", "tired"),
    (True, "faux", "fausse", "untrue"),
    (False, "fidèle", "fidèle", "faithful"),
    (False, "fier", "fière", "excited"),
    (False, "frustré", "frustrée", "frustrated"),
    (False, "gêné", "gênée", "embarrassed"),
    (False, "gentil", "gentille", "kind"),
    (False, "heureux", "heureuse", "happy"),
    (False, "horrible", "horrible", "dreadful"),
    (False, "indisposé", "indisposée", "indisposed"),
    (False, "jovial", "joviale", "cheerful"),
    (False, "joyeux", "joyeuse", "joyful"),
    (False, "las", "lasse", "weary"),
    (False, "malade", "malade", "sick"),
    (False, "malicieux", "malicieuse", "mischievous"),
    (False, "mature", "mature", "mature"),
    (False, "mauvais", "mauvaise", "bad"),
    (True, "méchant", "méchante", "mean"),
    (False, "pacifique", "pacifique", "peaceful"),
    (False, "peiné", "peinée", "saddened"),
    (False, "perplexe", "perplexe", "puzzled"),
    (False, "perturbé", "perturbée", "disturbed"),
    (False, "prétentieux", "prétentieuse", "pretentious"),
    (False, "prudent", "prudente", "careful"),
    (False, "rieur", "rieuse", "joking"),
    (False, "solitaire", "solitaire", "lonely"),
    (False, "soucieux", "soucieuse", "concerned"),
    (False, "souffrant", "souffrante", "ailing"),
    (False, "soupçonneux", "soupçonneuse", "suspicious"),
    (False, "sûr", "sûre", "reliable"),
    (False, "discret", "discrète", "understated"),
    (False, "tranquille", "tranquille", "quiet"),
    (False, "triste", "triste", "sad"),
    (False, "troublé", "troublée", "troubled"),
    (False, "altéré", "altérée", "altered"),
    (False, "circulaire", "circulaire", "circular"),
    (False, "creux", "creuse", "hollow"),
    (False, "décomposé", "décomposée", "decomposed"),
    (False, "déformé", "déformée", "distorted"),
    (False, "droit", "droite", "right"),
    (False, "étroit", "étroite", "close"),
    (False, "géométrique", "géométrique", "geometric"),
    (True, "long", "longue", "lengthy"),
    (False, "maigre", "maigre", "meagre"),
    (False, "plat", "plate", "flat"),
    (False, "primitif", "primitive", "primitive"),
    (False, "raide", "raide", "stiff"),
    (False, "rectangulaire", "rectangulaire", "rectangular"),
    (False, "rond", "ronde", "round"),
    (False, "simple", "simple", "simple"),
    (False, "tordu", "tordue", "twisted"),
    (False, "triangulaire", "triangulaire", "triangular"),
    (True, "vaste", "vaste", "extensive"),
    (False, "colossal", "colossale", "huge"),
    (False, "énorme", "énorme", "huge"),
    (False, "exigu", "exigue", "cramped"),
    (False, "fin", "fine", "thin"),
    (False, "gigantesque", "gigantesque", "gigantic"),
    (True, "grand", "grande", "great"),
    (True, "immense", "immense", "immense"),
    (False, "important", "importante", "significant"),
    (False, "imposant", "imposante", "imposing"),
    (False, "infime", "infime", "tiny"),
    (True, "large", "large", "wide"),
    (False, "menu", "menue", "small"),
    (True, "minuscule", "minuscule", "lowercase"),
    (False, "monumental", "monumentale", "monumental"),
    (True, "petit", "petite", "little"),
    (True, "chouette", "chouette", "fun"),
    (True, "super", "super", "great"),
    (False, "vaste", "vaste", "extensive"),
    (False, "actuel", "actuelle", "current"),
    (False, "ancien", "ancienne", "former"),
    (False, "annuel", "annuelle", "yearly"),
    (False, "antique", "antique", "ancient"),
    (False, "avancé", "avancée", "advanced"),
    (False, "contemporain", "contemporaine", "contemporary"),
    (False, "hebdomadaire", "hebdomadaire", "weekly"),
    (True, "jeune", "jeune", "young"),
    (False, "journalier", "journalière", "daily"),
    (False, "lent", "lente", "slow"),
    (False, "mensuel", "mensuelle", "monthly"),
    (False, "moderne", "moderne", "modern"),
    (False, "neuf", "neuve", "new"),
    (False, "nouveau", "nouvelle", "new"),
    (False, "précipité", "précipitée", "hasty"),
    (False, "précis", "précise", "specific"),
    (False, "idoine", "idoine", "appropriate"),
    (False, "prompt", "prompte", "prompt"),
    (False, "quotidien", "quotidienne", "daily"),
    (False, "rapide", "rapide", "quick"),
    (False, "alerte", "alerte", "alert"),
    (False, "preste", "preste", "nimble"),
    (False, "récent", "récente", "recent"),
    (False, "séculaire", "séculaire", "secular"),
    (False, "tardif", "tardive", "late"),
    (False, "trimestriel", "trimestrielle", "quarterly"),
    (False, "vétuste", "vétuste", "dilapidated"),
    (True, "vieux/vieil", "vieille", "old"),
    (False, "abondant", "abondante", "plentiful"),
    (False, "bienfaisant", "bienfaisante", "beneficial"),
    (False, "chargé", "chargée", "busy"),
    (False, "compact", "compacte", "compact"),
    (False, "considérable", "considérable", "significant"),
    (False, "dense", "dense", "dense"),
    (False, "écrasant", "écrasante", "overwhelming"),
    (True, "énorme", "énorme", "huge"),
    (True, "extra", "extra", "extra"),
    (False, "fréquent", "fréquente", "frequent"),
    (True, "gros", "grosse", "large"),
    (False, "illimité", "illimitée", "unlimited"),
    (False, "incalculable", "incalculable", "incalculable"),
    (False, "léger", "légère", "lightweight"),
    (True, "lourd", "lourde", "major"),
    (False, "multiple", "multiple", "multifaceted"),
    (False, "rempli", "remplie", "completed"),
    (False, "substantiel", "substantielle", "substantial"),
    (False, "répété", "répétée", "repeated"),
    (False, "vide", "vide", "empty"),
    (False, "volumineux", "volumineuse", "voluminous"),
    (False, "argenté", "argentée", "silvery"),
    (False, "azuré", "azuré", "azure"),
    (False, "blanc", "blanche", "white"),
    (False, "bleu", "bleue", "blue"),
    (False, "blond", "blonde", "blonde"),
    (False, "brun", "brune", "brunette"),
    (False, "châtain", "châtaine", "chestnut"),
    (False, "cyan", "cyan", "cyan"),
    (False, "grenat", "grenat", "garnet"),
    (False, "magenta", "magenta", "magenta"),
    (False, "marron", "marron", "brown"),
    (False, "noir", "noire", "black"),
    (False, "orange", "orange", "orange"),
    (False, "pourpré", "pourprée", "purple"),
    (False, "rose", "rose", "pink"),
    (False, "roux", "rousse", "redhead"),
    (False, "turquoise", "turquoise", "turquoise"),
    (False, "vert", "verte", "green"),
    (False, "violet", "violette", "violet"),
    (False, "multilingue", "multilingue", "multilingual"),
    (False, "bilingue", "bilingue", "bilingual"),
    (False, "plurilingue", "plurilingue", "multilingual"),
    (False, "polyglotte", "polyglotte", "multilingual"),
    (False, "érudit", "érudite", "savant"),
    (False, "savant", "savante", "scholarly"),
    (False, "philosophe", "philosophe", "philosopher"),
    (False, "studieux", "studieuse", "studious"),
    (False, "instruit", "instruite", "educated"),
    (False, "lettré", "lettrée", "literate"),
    (False, "cultivé", "cultivée", "cultivated"),
    (False, "clairvoyant", "clairvoyante", "clairvoyant"),
    (False, "expert", "experte", "expert"),
    (False, "ingénieux", "ingénieuse", "ingenious"),
    (False, "compétent", "compétente", "competent"),
    (False, "scientifique", "scientifique", "scientific"),
    (False, "chercheur", "chercheuse", "researcher"),
    (False, "spécialiste", "spécialiste", "expert"),
    (False, "humaniste", "humaniste", "humanist"),
    (True, "maître", "maîtresse", "mistress"),
    (False, "câlé", "câlée", "cabled"),
    (False, "intelligent", "intelligente", "smart"),
    (False, "averti", "avertie", "knowledgeable"),
    (False, "fortiche", "fortiche", "fortiche"),
    (False, "habile", "habile", "skillful"),
    (False, "travailleur", "travailleuse", "worker"),
    (False, "drôle", "drôle", "funny"),
    (False, "égayant", "égayant", "brightening"),
    (False, "drôlet", "drôlette", "funny"),
    (False, "cocasse", "cocasse", "funny"),
    (False, "désopilant", "désopilant", "hilarious"),
    (False, "facétieux", "facétieuse", "facetious"),
    (False, "marrant", "marrante", "funny"),
    (False, "tordant", "tordante", "hilarious"),
    (False, "comique", "comique", "comic"),
    (False, "spirituel", "spirituelle", "spiritual"),
    (False, "insolite", "insolite", "unusual"),
    (False, "bizarre", "bizarre", "weird"),
    (True, "étrange", "étrange", "strange"),
    (False, "curieux", "curieuse", "inquisitive"),
    (False, "docte", "docte", "erudite"),
    (False, "juste", "juste", "rightly"),
    (False, "paisible", "paisible", "peaceful"),
    (False, "sagace", "sagace", "wise"),
    (False, "ascète", "ascète", "ascetic"),
    (False, "honnête", "honnête", "honest"),
    (True, "honnête", "honnête", "honest")
]


def CapitalizeASCII(word):
    word = word.replace("é", "e").replace("è", "e").replace("ê", "e")
    word = word.replace("û", "u").replace("î", "i").replace("ï", "i").replace("â", "a")
    word = word.replace("ç", "c")
    return word[:1].upper()+word[1:]


def generate_name_fr(length=15):
    while True:
        gender, realnoun, tradnoun = random.choice(nouns)
        normnoun = realnoun.replace("-", "").replace(" ", "")
        left, adj_m, adj_f, tradadj = random.choice(adjs)
        if gender:
            adj = adj_m
        else:
            adj = adj_f
        realadj = adj
        # don't convert end-é into e - too ambiguous to read
        if adj.endswith("é"):
            continue
        adj = CapitalizeASCII(adj)
        noun = CapitalizeASCII(normnoun)
        if left:
            adj_forms = adj.split("/")
            if len(adj_forms) == 2:
                if re.match(r"^[AEIOUH]", noun):
                    adj = CapitalizeASCII(adj_forms[1])
                else:
                    adj = adj_forms[0]
            name = adj + noun
            realname = realadj+" "+realnoun
        else:
            name = noun + adj
            realname = realnoun+" "+realadj
        trad = tradadj+" "+tradnoun
        if len(name) <= length and re.match(r"[A-Z][a-z]+[A-Z][a-z]+$", name):
            return (name, realname, trad)


if __name__ == "__main__":
    for i in range(100):
        print "\t".join(generate_name_fr())