#EXTRA CLASS
class MnemonicValidator:
  mnemonic_word_list = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract", "absurd", "abuse",
    "access", "accident", "account", "accuse", "achieve", "acid", "acoustic", "acquire", "across", "act",
    "action", "actor", "actress", "actual", "adapt", "add", "addict", "address", "adjust", "admit",
    "adult", "advance", "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
    "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert",
    "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also", "alter",
    "always", "amateur", "amazing", "among", "amount", "amused", "analyst", "anchor", "ancient", "anger",
    "angle", "angry", "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique",
    "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april", "arch", "arctic",
    "area", "arena", "argue", "arm", "armed", "armor", "army", "around", "arrange", "arrest",
    "arrive", "arrow", "art", "artefact", "artist", "artwork", "ask", "aspect", "assault", "asset",
    "assist", "assume", "asthma", "athlete", "atom", "attack", "attend", "attitude", "attract", "auction",
    "audit", "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid", "awake",
    "aware", "away", "awesome", "awful", "awkward", "axis", "baby", "bachelor", "bacon", "badge",
    "bag", "balance", "balcony", "ball", "bamboo", "banana", "banner", "bar", "barely", "bargain",
    "barrel", "base", "basic", "basket", "battle", "beach", "bean", "beauty", "because", "become",
    "beef", "before", "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit",
    "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike", "bind", "biology",
    "bird", "birth", "bitter", "black", "blade", "blame", "blanket", "blast", "bleak", "bless",
    "blind", "blood", "blossom", "blouse", "blue", "blur", "blush", "board", "boat", "body",
    "boil", "bomb", "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss",
    "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brass", "brave", "bread",
    "breeze", "brick", "bridge", "brief", "bright", "bring", "brisk", "broccoli", "broken", "bronze",
    "broom", "brother", "brown", "brush", "bubble", "buddy", "budget", "buffalo", "build", "bulb",
    "bulk", "bullet", "bundle", "bunker", "burden", "burger", "burst", "bus", "business", "busy",
    "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus", "cage", "cake", "call",
    "calm", "camera", "camp", "can", "canal", "cancel", "candy", "cannon", "canoe", "canvas",
    "canyon", "capable", "capital", "captain", "car", "carbon", "card", "cargo", "carpet", "carry",
    "cart", "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category",
    "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement", "census", "century",
    "cereal", "certain", "chair", "chalk", "champion", "change", "chaos", "chapter", "charge", "chase",
    "chat", "cheap", "check", "cheese", "chef", "cherry", "chest", "chicken", "chief", "child",
    "chimney", "choice", "choose", "chronic", "chuckle", "chunk", "churn", "cigar", "cinnamon", "circle",
    "citizen", "city", "civil", "claim", "clap", "clarify", "claw", "clay", "clean", "clerk",
    "clever", "click", "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close",
    "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast", "coconut",
    "code", "coffee", "coil", "coin", "collect", "color", "column", "combine", "come", "comfort",
    "comic", "common", "company", "concert", "conduct", "confirm", "congress", "connect", "consider", "control",
    "convince", "cook", "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost",
    "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack", "cradle",
    "craft", "cram", "crane", "crash", "crater", "crawl", "crazy", "cream", "credit", "creek",
    "crew", "cricket", "crime", "crisp", "critic", "crop", "cross", "crouch", "crowd", "crucial",
    "cruel", "cruise", "crumble", "crunch", "crush", "cry", "crystal", "cube", "culture", "cup",
    "cupboard", "curious", "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad",
    "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn", "day", "deal",
    "debate", "debris", "decade", "december", "decide", "decline", "decorate", "decrease", "deer", "defense",
    "define", "defy", "degree", "delay", "deliver", "demand", "demise", "denial", "dentist", "deny",
    "depart", "depend", "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk",
    "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram", "dial", "diamond",
    "diary", "dice", "diesel", "diet", "differ", "digital", "dignity", "dilemma", "dinner", "dinosaur",
    "direct", "dirt", "disagree", "discover", "disease", "dish", "dismiss", "disorder", "display", "distance",
    "divert", "divide", "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain",
    "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft", "dragon", "drama",
    "drastic", "draw", "dream", "dress", "drift", "drill", "drink", "drip", "drive", "drop",
    "drum", "dry", "duck", "dumb", "dune", "during", "dust", "dutch", "duty", "dwarf",
    "dynamic", "eager", "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo",
    "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight", "either", "elbow",
    "elder", "electric", "elegant", "element", "elephant", "elevator", "elite", "else", "embark", "embody",
    "embrace", "emerge", "emotion", "employ", "empower", "empty", "enable", "enact", "end", "endless",
    "endorse", "enemy", "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough",
    "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode", "equal", "equip",
    "era", "erase", "erode", "erosion", "error", "erupt", "escape", "essay", "essence", "estate",
    "eternal", "ethics", "evidence", "evil", "evoke", "evolve", "exact", "example", "excess", "exchange",
    "excite", "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit",
    "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend", "extra", "eye",
    "eyebrow", "fabric", "face", "faculty", "fade", "faint", "faith", "fall", "false", "fame",
    "family", "famous", "fan", "fancy", "fantasy", "farm", "fashion", "fat", "fatal", "father",
    "fatigue", "fault", "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female",
    "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field", "figure", "file",
    "film", "filter", "final", "find", "fine", "finger", "finish", "fire", "firm", "first",
    "fiscal", "fish", "fit", "fitness", "fix", "flag", "flame", "flash", "flat", "flavor",
    "flee", "flight", "flip", "float", "flock", "floor", "flower", "fluid", "flush", "fly",
    "foam", "focus", "fog", "foil", "fold", "follow", "food", "foot", "force", "forest",
    "forget", "fork", "fortune", "forum", "forward", "fossil", "foster", "found", "fox", "fragile",
    "frame", "frequent", "fresh", "friend", "fringe", "frog", "front", "frost", "frown", "frozen",
    "fruit", "fuel", "fun", "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy",
    "gallery", "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas", "gasp",
    "gate", "gather", "gauge", "gaze", "general", "genius", "genre", "gentle", "genuine", "gesture",
    "ghost", "giant", "gift", "giggle", "ginger", "giraffe", "girl", "give", "glad", "glance",
    "glare", "glass", "glide", "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue",
    "goat", "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern", "gown",
    "grab", "grace", "grain", "grant", "grape", "grass", "gravity", "great", "green", "grid",
    "grief", "grit", "grocery", "group", "grow", "grunt", "guard", "guess", "guide", "guilt",
    "guitar", "gun", "gym", "habit", "hair", "half", "hammer", "hamster", "hand", "happy",
    "harbor", "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head", "health",
    "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help", "hen", "hero", "hidden",
    "high", "hill", "hint", "hip", "hire", "history", "hobby", "hockey", "hold", "hole",
    "holiday", "hollow", "home", "honey", "hood", "hope", "horn", "horror", "horse", "hospital",
    "host", "hotel", "hour", "hover", "hub", "huge", "human", "humble", "humor", "hundred",
    "hungry", "hunt", "hurdle", "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea",
    "identify", "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense", "immune",
    "impact", "impose", "improve", "impulse", "inch", "include", "income", "increase", "index", "indicate",
    "indoor", "industry", "infant", "inflict", "inform", "inhale", "inherit", "initial", "inject", "injury",
    "inmate", "inner", "innocent", "input", "inquiry", "insane", "insect", "inside", "inspire", "install",
    "intact", "interest", "into", "invest", "invite", "involve", "iron", "island", "isolate", "issue",
    "item", "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly", "jewel",
    "job", "join", "joke", "journey", "joy", "judge", "juice", "jump", "jungle", "junior",
    "junk", "just", "kangaroo", "keen", "keep", "ketchup", "key", "kick", "kid", "kidney",
    "kind", "kingdom", "kiss", "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife",
    "knock", "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp", "language",
    "laptop", "large", "later", "latin", "laugh", "laundry", "lava", "law", "lawn", "lawsuit",
    "layer", "lazy", "leader", "leaf", "learn", "leave", "lecture", "left", "leg", "legal",
    "legend", "leisure", "lemon", "lend", "length", "lens", "leopard", "lesson", "letter", "level",
    "liar", "liberty", "library", "license", "life", "lift", "light", "like", "limb", "limit",
    "link", "lion", "liquid", "list", "little", "live", "lizard", "load", "loan", "lobster",
    "local", "lock", "logic", "lonely", "long", "loop", "lottery", "loud", "lounge", "love",
    "loyal", "lucky", "luggage", "lumber", "lunar", "lunch", "luxury", "lyrics", "machine", "mad",
    "magic", "magnet", "maid", "mail", "main", "major", "make", "mammal", "man", "manage",
    "mandate", "mango", "mansion", "manual", "maple", "marble", "march", "margin", "marine", "market",
    "marriage", "mask", "mass", "master", "match", "material", "math", "matrix", "matter", "maximum",
    "maze", "meadow", "mean", "measure", "meat", "mechanic", "medal", "media", "melody", "melt",
    "member", "memory", "mention", "menu", "mercy", "merge", "merit", "merry", "mesh", "message",
    "metal", "method", "middle", "midnight", "milk", "million", "mimic", "mind", "minimum", "minor",
    "minute", "miracle", "mirror", "misery", "miss", "mistake", "mix", "mixed", "mixture", "mobile",
    "model", "modify", "mom", "moment", "monitor", "monkey", "monster", "month", "moon", "moral",
    "more", "morning", "mosquito", "mother", "motion", "motor", "mountain", "mouse", "move", "movie",
    "much", "muffin", "mule", "multiply", "muscle", "museum", "mushroom", "music", "must", "mutual",
    "myself", "mystery", "myth", "naive", "name", "napkin", "narrow", "nasty", "nation", "nature",
    "near", "neck", "need", "negative", "neglect", "neither", "nephew", "nerve", "nest", "net",
    "network", "neutral", "never", "news", "next", "nice", "night", "noble", "noise", "nominee",
    "noodle", "normal", "north", "nose", "notable", "note", "nothing", "notice", "novel", "now",
    "nuclear", "number", "nurse", "nut", "oak", "obey", "object", "oblige", "obscure", "observe",
    "obtain", "obvious", "occur", "ocean", "october", "odor", "off", "offer", "office", "often",
    "oil", "okay", "old", "olive", "olympic", "omit", "once", "one", "onion", "online",
    "only", "open", "opera", "opinion", "oppose", "option", "orange", "orbit", "orchard", "order",
    "ordinary", "organ", "orient", "original", "orphan", "ostrich", "other", "outdoor", "outer", "output",
    "outside", "oval", "oven", "over", "own", "owner", "oxygen", "oyster", "ozone", "pact",
    "paddle", "page", "pair", "palace", "palm", "panda", "panel", "panic", "panther", "paper",
    "parade", "parent", "park", "parrot", "party", "pass", "patch", "path", "patient", "patrol",
    "pattern", "pause", "pave", "payment", "peace", "peanut", "pear", "peasant", "pelican", "pen",
    "penalty", "pencil", "people", "pepper", "perfect", "permit", "person", "pet", "phone", "photo",
    "phrase", "physical", "piano", "picnic", "picture", "piece", "pig", "pigeon", "pill", "pilot",
    "pink", "pioneer", "pipe", "pistol", "pitch", "pizza", "place", "planet", "plastic", "plate",
    "play", "please", "pledge", "pluck", "plug", "plunge", "poem", "poet", "point", "polar",
    "pole", "police", "pond", "pony", "pool", "popular", "portion", "position", "possible", "post",
    "potato", "pottery", "poverty", "powder", "power", "practice", "praise", "predict", "prefer", "prepare",
    "present", "pretty", "prevent", "price", "pride", "primary", "print", "priority", "prison", "private",
    "prize", "problem", "process", "produce", "profit", "program", "project", "promote", "proof", "property",
    "prosper", "protect", "proud", "provide", "public", "pudding", "pull", "pulp", "pulse", "pumpkin",
    "punch", "pupil", "puppy", "purchase", "purity", "purpose", "purse", "push", "put", "puzzle",
    "pyramid", "quality", "quantum", "quarter", "question", "quick", "quit", "quiz", "quote", "rabbit",
    "raccoon", "race", "rack", "radar", "radio", "rail", "rain", "raise", "rally", "ramp",
    "ranch", "random", "range", "rapid", "rare", "rate", "rather", "raven", "raw", "razor",
    "ready", "real", "reason", "rebel", "rebuild", "recall", "receive", "recipe", "record", "recycle",
    "reduce", "reflect", "reform", "refuse", "region", "regret", "regular", "reject", "relax", "release",
    "relief", "rely", "remain", "remember", "remind", "remove", "render", "renew", "rent", "reopen",
    "repair", "repeat", "replace", "report", "require", "rescue", "resemble", "resist", "resource", "response",
    "result", "retire", "retreat", "return", "reunion", "reveal", "review", "reward", "rhythm", "rib",
    "ribbon", "rice", "rich", "ride", "ridge", "rifle", "right", "rigid", "ring", "riot",
    "ripple", "risk", "ritual", "rival", "river", "road", "roast", "robot", "robust", "rocket",
    "romance", "roof", "rookie", "room", "rose", "rotate", "rough", "round", "route", "royal",
    "rubber", "rude", "rug", "rule", "run", "runway", "rural", "sad", "saddle", "sadness",
    "safe", "sail", "salad", "salmon", "salon", "salt", "salute", "same", "sample", "sand",
    "satisfy", "satoshi", "sauce", "sausage", "save", "say", "scale", "scan", "scare", "scatter",
    "scene", "scheme", "school", "science", "scissors", "scorpion", "scout", "scrap", "screen", "script",
    "scrub", "sea", "search", "season", "seat", "second", "secret", "section", "security", "seed",
    "seek", "segment", "select", "sell", "seminar", "senior", "sense", "sentence", "series", "service",
    "session", "settle", "setup", "seven", "shadow", "shaft", "shallow", "share", "shed", "shell",
    "sheriff", "shield", "shift", "shine", "ship", "shiver", "shock", "shoe", "shoot", "shop",
    "short", "shoulder", "shove", "shrimp", "shrug", "shuffle", "shy", "sibling", "sick", "side",
    "siege", "sight", "sign", "silent", "silk", "silly", "silver", "similar", "simple", "since",
    "sing", "siren", "sister", "situate", "six", "size", "skate", "sketch", "ski", "skill",
    "skin", "skirt", "skull", "slab", "slam", "sleep", "slender", "slice", "slide", "slight",
    "slim", "slogan", "slot", "slow", "slush", "small", "smart", "smile", "smoke", "smooth",
    "snack", "snake", "snap", "sniff", "snow", "soap", "soccer", "social", "sock", "soda",
    "soft", "solar", "soldier", "solid", "solution", "solve", "someone", "song", "soon", "sorry",
    "sort", "soul", "sound", "soup", "source", "south", "space", "spare", "spatial", "spawn",
    "speak", "special", "speed", "spell", "spend", "sphere", "spice", "spider", "spike", "spin",
    "spirit", "split", "spoil", "sponsor", "spoon", "sport", "spot", "spray", "spread", "spring",
    "spy", "square", "squeeze", "squirrel", "stable", "stadium", "staff", "stage", "stairs", "stamp",
    "stand", "start", "state", "stay", "steak", "steel", "stem", "step", "stereo", "stick",
    "still", "sting", "stock", "stomach", "stone", "stool", "story", "stove", "strategy", "street",
    "strike", "strong", "struggle", "student", "stuff", "stumble", "style", "subject", "submit", "subway",
    "success", "such", "sudden", "suffer", "sugar", "suggest", "suit", "summer", "sun", "sunny",
    "sunset", "super", "supply", "supreme", "sure", "surface", "surge", "surprise", "surround", "survey",
    "suspect", "sustain", "swallow", "swamp", "swap", "swarm", "swear", "sweet", "swift", "swim",
    "swing", "switch", "sword", "symbol", "symptom", "syrup", "system", "table", "tackle", "tag",
    "tail", "talent", "talk", "tank", "tape", "target", "task", "taste", "tattoo", "taxi",
    "teach", "team", "tell", "ten", "tenant", "tennis", "tent", "term", "test", "text",
    "thank", "that", "theme", "then", "theory", "there", "they", "thing", "this", "thought",
    "three", "thrive", "throw", "thumb", "thunder", "ticket", "tide", "tiger", "tilt", "timber",
    "time", "tiny", "tip", "tired", "tissue", "title", "toast", "tobacco", "today", "toddler",
    "toe", "together", "toilet", "token", "tomato", "tomorrow", "tone", "tongue", "tonight", "tool",
    "tooth", "top", "topic", "topple", "torch", "tornado", "tortoise", "toss", "total", "tourist",
    "toward", "tower", "town", "toy", "track", "trade", "traffic", "tragic", "train", "transfer",
    "trap", "trash", "travel", "tray", "treat", "tree", "trend", "trial", "tribe", "trick",
    "trigger", "trim", "trip", "trophy", "trouble", "truck", "true", "truly", "trumpet", "trust",
    "truth", "try", "tube", "tuition", "tumble", "tuna", "tunnel", "turkey", "turn", "turtle",
    "twelve", "twenty", "twice", "twin", "twist", "two", "type", "typical", "ugly", "umbrella",
    "unable", "unaware", "uncle", "uncover", "under", "undo", "unfair", "unfold", "unhappy", "uniform",
    "unique", "unit", "universe", "unknown", "unlock", "until", "unusual", "unveil", "update", "upgrade",
    "uphold", "upon", "upper", "upset", "urban", "urge", "usage", "use", "used", "useful",
    "useless", "usual", "utility", "vacant", "vacuum", "vague", "valid", "valley", "valve", "van",
    "vanish", "vapor", "various", "vast", "vault", "vehicle", "velvet", "vendor", "venture", "venue",
    "verb", "verify", "version", "very", "vessel", "veteran", "viable", "vibrant", "vicious", "victory",
    "video", "view", "village", "vintage", "violin", "virtual", "virus", "visa", "visit", "visual",
    "vital", "vivid", "vocal", "voice", "void", "volcano", "volume", "vote", "voyage", "wage",
    "wagon", "wait", "walk", "wall", "walnut", "want", "warfare", "warm", "warrior", "wash",
    "wasp", "waste", "water", "wave", "way", "wealth", "weapon", "wear", "weasel", "weather",
    "web", "wedding", "weekend", "weird", "welcome", "west", "wet", "whale", "what", "wheat",
    "wheel", "when", "where", "whip", "whisper", "wide", "width", "wife", "wild", "will",
    "win", "window", "wine", "wing", "wink", "winner", "winter", "wire", "wisdom", "wise",
    "wish", "witness", "wolf", "woman", "wonder", "wood", "wool", "word", "work", "world",
    "worry", "worth", "wrap", "wreck", "wrestle", "wrist", "write", "wrong", "yard", "year",
    "yellow", "you", "young", "youth", "zebra", "zero", "zone", "zoo"]

  mnemonic_black_list = [
    'this just best time invest earn that when coin again then more',
    'also that this project list token they just say give people any correct',
    'can invest any amount this company never have worry about because you sure that',
    'have never this kind act second one that help there any way',
    'thing have always about matter time you start must still good amount',
    'will make another deposit right now can able receive profit good work',
    'what you suggest little project that can help village have minute cost',
    'have reject lobster horse deputy universe dragon move alarm clip radar peanut glide',
    'never thought have that same believe there good where one invest make',
    'can teach you all now make just smart phone please only once',
    'theory you can hold long have capital avoid this correct way trade',
    'need off few this like rapid fire speed all bullet more will',
    'they pretty much people that strategy man you feel urge unlock all',
    'thing love about this that matter time you can always make profit',
    'will advice join invest this company they have one day very awesome',
    'day have always come only that they can earn more this just',
    'this best have what great company talent please keep good work agent',
    'day people say good about this company very news because what all want',
    'good only because once you have agent hand then life very easy',
    'nose dog tree cat book sun rain pen cup moon desk lamp door key car ball fish bird sock hat shoe hand',
    'can drink more water when you explain talk much feel will very hard',
    'hello you have special day off next please write will update tomorrow',
    'team great job now you turn just hold panic sell wait few',
    'win more better other make smile again they before still run away',
    'love way you work invest must they trust all heart because know',
    'they cook now there head chef learn what dish you can make',
    'make this quick cool bread still online come place high balance always',
    'two strong like stone soft chalk when erode above fall step then',
    'love this company they make sure payment want invest again same process',
    'feel much better about someone like this great work you again unique',
    'will rather invest else because other company can give you good quality like',
    'please next time ask when you any make sure street that can entire',
    'core team must come solution that sell still they have token balance',
    'great myself want have more two will very much during next run',
    'below always middle hungry wage quick goddess struggle ladder glow elder fence trumpet ozone room egg pyramid uniform cousin summer invest scare fluid'
  ]

  def get_intersect_list(self, words_list):
    # logging.info("checking for min_num of mnemonic matches in words <%s>", words_list)
    intersec_list = set(words_list).intersection(self.mnemonic_word_list)

    return intersec_list

  def check_for_mnemonic_words(self, words_list, min_num):
    # logging.info("checking for min_num <%d> of mnemonic matches in words <%s>", min_num, words_list)
    intersec_list = self.get_intersect_list(words_list)
    words_position_list = []
    if len(intersec_list) >= min_num:
      ret = True
      for word in intersec_list:
        word_position = words_list.index(word)
        words_position_list.append(word_position)
      words_position_list.sort()
    else:
      ret = False
      words_position_list = None

    return ret, intersec_list, words_position_list


class CryptoCoinWordMatchType:
  BITCOIN = "BITCOIN"
  BITCOIN_TRX_ID = "BITCOIN_TRX_ID"
  BITCOIN_BASE58 = "BITCOIN_BASE58"
  BITCOIN_BECH32 = "BITCOIN_BECH32"
  ETHEREUM = "ETHEREUM"
  MONERO = "MONERO"
  ZCASH_T = "ZCASH_T_BASE58"
  ZCASH_Z = "ZCASH_Z_BECH32"
  LITECOIN = "LITECOIN"
  RIPPLE = "RIPPLE"
  BITCOIN_CASH = "BITCOIN_CASH"
  MNEMONIC_PHRASE = "MNEMONIC_PHRASE"
  XPUB = "XPUB"
  WIF = "WIF_PRIVATE_KEY"
  TRON = "TRON"
  IBAN = "IBAN"
  VISA = "VISA"
  MASTERCARD = "MASTERCARD"
  CONTAINER = "CONTAINER"
  CREDIT_CARD = "CREDIT_CARD"

class WebAddressWordMatchType:
  WEB_ADDRESS = "WEB_ADDRESS"


class InstalledApplicationMatchType:
  INSTALLED_APPLICATION = "INSTALLED_APPLICATION"
  DIR_LIST_APPLICATION = "DIR_LIST_APPLICATION"


class UserCredentialsMatchType:
  USER_CREDENTIALS = "USER_CREDENTIALS"


class MatchGroupType:
  COINS_GROUP = "CRYPTO_COINS"
  WEB_ACTIVITY_GROUP = "WEB_ACTIVITY"
  MNEMONIC_GROUP = "MNEMONIC"
  APPLICATION_ACTIVITY_GROUP = "APPLICATION_ACTIVITY"
  USER_CREDENTIALS_GROUP = "USER_CREDENTIALS"
  XPUB_GROUP = "XPUB"
  BANKING = "BANKING"
  CREDITCARD = "CREDITCARD"
  COMMERCE = "COMMERCE"


class RawTextAnalyzerConsts:
  # MinLen = 26
  WordMaxStartPos = 5
  WordMaxEndGap = 5
  BitcoinMinLen = 14  # for both bech32 and base58
  BitcoinMaxLen = 74  # for both bech32 and base58
  EthereumMinLen = 40
  EthereumMaxLen = 40
  TronMinLen = 34
  TronMaxLen = 34
  IbanMinLen = 5
  CreditCardMinLen = 8
  ContainerMinLen = 11
  BitCoinCashMinLen = 42
  BitCoinCashMaxLen = 54
  BitcoinTrxIdLength = 64
  MoneroMinLen = 95
  MoneroMaxLen = 106
  ZcashTMinLen = 35
  ZcashTMaxLen = 35
  ZcashZMinLen = 78
  ZcashZMaxLen = 78
  WifMinLen = 51
  RippleMinLen = 26
  RippleMaxLen = 36
  LiteCoinMinLen = 26
  LiteCoinMaxLen = 59
  XpubMinLen = 50
  XpubMaxLen = 112
  WordGenMinLen = min([BitcoinMinLen, EthereumMinLen, MoneroMinLen, ZcashTMinLen, ZcashZMinLen, LiteCoinMinLen,
                       RippleMinLen, BitCoinCashMinLen, XpubMinLen, BitcoinTrxIdLength, TronMinLen,IbanMinLen,ContainerMinLen])
  WordGenMaxLen = max([BitcoinMaxLen, EthereumMaxLen, MoneroMaxLen, ZcashTMaxLen, ZcashZMaxLen, LiteCoinMaxLen,
                       RippleMaxLen, BitCoinCashMaxLen, XpubMaxLen, BitcoinTrxIdLength,TronMaxLen])
  ContextWordsListLen = 5  # how many words before and after match word to display in context part
  PrefixContextLen = 50
  PostfixContextLen = 50
  MnemonicPossibleLenList = [12, 24]
  Base58PreFixList = ["1", "3"]
  BECH32PrefixList = ["bc1"]
  EthereumPrefixList = ["0x"]
  TronPrefixList = ["T","t"]
  ZCashPrefixList = ["zs1", "t1", "t3"]
  BitCoinCashPrefixList = ["bitcoincash:", "BITCOINCASH:"]
  # RegExPatternEmail = r'(l|a)\S+@\S.\S+'  # email starting with l or a
  RegExPatternEmail = r'\S+@\S+.\S+'  # email
  RegExPattern32bitsHash = r'([a-fA-F\d]{32})'  # 32bits hash
  RegExPattern64bitsHash = r'([a-fA-F\d]{64})'
  Mnemonic = r'(([a-zA-Z]{3,}[ \n\-;,\.]){23})([a-zA-Z]{3,})|(([a-zA-Z]{3,}[ \n\-;,\.]){11})([a-zA-Z]{3,})'
  BitcoinAddressOld = r'([13][a-km-z-A-HJ-NP-Z1-9]{25,34})'
  BitcoinAddressCurrent = r'([13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[ac-hj-np-zAC-HJ-NP-Z02-9]{23,71})'  # use ^ for exact start of word
  EthereumAddress = r'0x[a-fA-F0-9]{40}'
  Tron = r'(T|t)[a-zA-Z0-9]{33}'
  Iban_old = r'(?:[^0-9a-zA-Z\/]|^)(A[Tt]|[Uu][Aa]|[Aa][Zz]|[Aa][Ee]|[Ii][Tt]|[Vv][Gg]|[Ff][Oo]|I[Ss]|[Ii][Ee]|[Ss][Vv]|[Aa][Ll]|[Aa][Dd]|[Ee][Ee]|[Bb][Gg]|[Bb][Aa]|[Bb][Hh]|[Bb][Ee]|B[Yy]|[Bb][Rr]|[Gg][Bb]|[Gg][Ee]|[Gg][Tt]|[Gg][Ii]|[Gg][Ll]|[Dd][Ee]|[Dd][Kk]|[Nn][Ll]|[Hh][Uu]|[Dd][Oo]|[Pp][Ss]|[Tt][Rr]|[Tt][Ll]|[Gg][Rr]|[Jj][Oo]|[Ii][Ll]|[Kk][Ww]|[Ll][Bb]|[Ll][Uu]|[Ll][Vv]|[Ll][Tt]|[Ll][Ii]|[Mm][Rr]|[Mm][Uu]|[Mm][Tt]|[Mm][Dd]|[Mm][Ee]|[Mm][Cc]|[Mm][Kk]|[Ss][Tt]|[Ss][Mm]|[Ss][Cc]|[Ss][Ii]|[Ss][Kk]|[Ll][Cc]|[Ee][Ss]|[Rr][Ss]|[Ii][Qq]|[Ss][Aa]|[Pp][Ll]|[Pp][Tt]|[Ff][Ii]|[Pp][Kk]|[Cc][Zz]|[Ff][Rr]|[Xx][Kk]|[Cc][Rr]|[Kk][Zz]|[Qq][Aa]|[Cc][Yy]|[Hh][Rr]|[Rr][Oo]|[Ss][Ee]|[Cc][Hh]|[Tt][Nn]|[Ii][Rr]|[Dd][Zz]|[Aa][Oo]|[Bb][Ii]|[Bb][Ff]|[Bb][Jj]|[Dd][Jj]|[Gg][Aa]|[Gg][Ww]|[Gg][Qq]|[Hh][Nn]|[Cc][Ff]|[Cc][Ii]|[Tt][Gg]|[Mm][Ll]|[Mm][Gg]|[Mm][Zz]|[Ee][Gg]|[Mm][Aa]|[Nn][Ee]|[Nn][Ii]|[Ss][Nn]|[Tt][Dd]|[Kk][Mm]|[Cc][Gg]|[Cc][Mm]|[Cc][Vv])[- ]?[0-9]{2}[- ]?[a-zA-Z0-9]{4}[- ]?[0-9]{4,7}[- ]?[0-9]{0,4}([- ]?[0-9]{4}){1,8}(?:[^0-9a-zA-Z]|$)'
  Iban = r'(?:[^0-9a-zA-Z\/]|^)(A[Tt]|[Uu][Aa]|[Aa][Zz]|[Aa][Ee]|[Ii][Tt]|[Vv][Gg]|[Ff][Oo]|I[Ss]|[Ii][Ee]|[Ss][Vv]|[Aa][Ll]|[Aa][Dd]|[Ee][Ee]|[Bb][Gg]|[Bb][Aa]|[Bb][Hh]|[Bb][Ee]|B[Yy]|[Bb][Rr]|[Gg][Bb]|[Gg][Ee]|[Gg][Tt]|[Gg][Ii]|[Gg][Ll]|[Dd][Ee]|[Dd][Kk]|[Nn][Ll]|[Hh][Uu]|[Dd][Oo]|[Pp][Ss]|[Tt][Rr]|[Tt][Ll]|[Gg][Rr]|[Jj][Oo]|[Ii][Ll]|[Kk][Ww]|[Ll][Bb]|[Ll][Uu]|[Ll][Vv]|[Ll][Tt]|[Ll][Ii]|[Mm][Rr]|[Mm][Uu]|[Mm][Tt]|[Mm][Dd]|[Mm][Ee]|[Mm][Cc]|[Mm][Kk]|[Ss][Tt]|[Ss][Mm]|[Ss][Cc]|[Ss][Ii]|[Ss][Kk]|[Ll][Cc]|[Ee][Ss]|[Rr][Ss]|[Ii][Qq]|[Ss][Aa]|[Pp][Ll]|[Pp][Tt]|[Ff][Ii]|[Pp][Kk]|[Cc][Zz]|[Ff][Rr]|[Xx][Kk]|[Cc][Rr]|[Kk][Zz]|[Qq][Aa]|[Cc][Yy]|[Hh][Rr]|[Rr][Oo]|[Ss][Ee]|[Cc][Hh]|[Tt][Nn]|[Ii][Rr]|[Dd][Zz]|[Aa][Oo]|[Bb][Ii]|[Bb][Ff]|[Bb][Jj]|[Dd][Jj]|[Gg][Aa]|[Gg][Ww]|[Gg][Qq]|[Hh][Nn]|[Cc][Ff]|[Cc][Ii]|[Tt][Gg]|[Mm][Ll]|[Mm][Gg]|[Mm][Zz]|[Ee][Gg]|[Mm][Aa]|[Nn][Oo]|[Nn][Ee]|[Nn][Ii]|[Ss][Nn]|[Tt][Dd]|[Kk][Mm]|[Cc][Gg]|[Cc][Mm]|[Cc][Vv])[- ]?[0-9]{2}[- ]?[a-zA-Z0-9]{4}[- ]?[0-9a-zA-Z]{1,}'
  Visa = '(?=((?:4[0-9]{12}(?:[0-9]{3})?)))'
  Mastercard = '(?=([25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}))'
  CreditCard_rlike = '((?:(?:[Cc]ard|CARD|طاقة|بطاقتك)| (?:(?:[Mm]aster|MASTER|[Vv]isa|VISA) (?:NO|[Nn]o)|كارد|كرت) ).{1,15}?#?([*0-9A-Za-z_(١)(٢)(٣)(٤)(٥)(٦)(٧)(٨)(٩)(٠)]{0,20}[0-9(١)(٢)(٣)(٤)(٥)(٦)(٧)(٨)(٩)(٠)]{3,20}[A-Z-a-z0-9_#*(١)(٢)(٣)(٤)(٥)(٦)(٧)(٨)(٩)(٠)]{0,20})|(?:[.]?4[0-9]{3}?[- ]*?[0-9]{4}?[- ]*?[0-9]{4}?[- ]*?[0-9]{4}?[- ]*?)|(?:[.]?[25][1-7][0-9]{2}?[- ]*[0-9]{4}?[- ]*[0-9]{4}?[- ]*[0-9]{4}))'
  Container = '([A-Z]{3}[JUZ][0-9]{7})'
  Xpub = '(xpub|xprv|ypub|zpub|zprv)[a-zA-Z0-9]{106,112}'
  MoneroAddress = r'[48][0-9AB][a-km-zA-HJ-NP-Z1-9]{93,104}'  # monero sub address can start with 8
  ZcashTAddress = r'(t1|t3)[1-9A-HJ-NP-Za-km-z]{33}'  # ZCash T address
  ZcashZAddress = r'zs1[ac-hj-np-zAC-HJ-NP-Z02-9]{74}'  # ZCash Zaddr
  RippleAddress = r'r[1-9a-km-zA-HJ-NP-Z]{25,35}'  # Ripple
  WifAddress = r'5[1-9a-km-zA-HJ-NP-Z]{50}|(L|K)[1-9a-km-zA-HJ-NP-Z]{51}'
  LiteCoinAddress = r'((L|M)[a-km-zA-HJ-NP-Z1-9]{25,34})|(ltc1([qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39}|[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{59}))'  # litecoin
  BitCoinCashAddress = r'((bitcoincash:)?(q|p)[a-z0-9]{41})|((BITCOINCASH:)?(Q|P)[A-Z0-9]{41})'
  GenWordsPrefixToIgnoreList = ["FolderCTID", "secret", "Secret"]
  XpubPrefixList = ["xprv", "xpub", "ypub", "yprv", "zpub", "zprv"]

class BlockScyParams:
  CheckWithBlockSci = True


class FileDictList:
  BASE_FILE_DICT_COL_LIST = [
    "run_mode",
    "raw_text"
  ]
  ERRORS_FILE_DICT_COL_LIST = [
    "exception",
    "file_size",
    "date_create",
    "date_modify",
    "raw_file_name"
  ]
  METADATA_COL_LIST = [
    "run_mode",
    "db_name",
    "table_name",
    "date_created",
    "date_on_field",
    "column_name",
    "row_id",
    "computer_id",
    "home_path"
  ]