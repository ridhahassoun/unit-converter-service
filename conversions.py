length = {
    "mi": {
        "yd": 1760,
        "ft": 5280,
        "in": 63360,
        "km": 1.609344,
        "m": 1609.344,
        "cm": 160934.4,
        "mm": 1609344
    },
    "yd": {
        "mi": 1 / 1760,
        "ft": 3,
        "in": 36,
        "km": 0.0009144,
        "m": 0.9144,
        "cm": 91.44,
        "mm": 914.4
    },
    "ft": {
        "mi": 1 / 5280,
        "yd": 1 / 3,
        "in": 12,
        "km": 0.0003048,
        "m": 0.3048,
        "cm": 30.48,
        "mm": 304.8
    },
    "in": {
        "mi": 1 / 63360,
        "yd": 1 / 36,
        "ft": 1 / 12,
        "km": 0.0000254,
        "m": 0.0254,
        "cm": 2.54,
        "mm": 25.4
    },
    "km": {
        "mi": 1 / 1.609344,
        "yd": 1 / 0.0009144,
        "ft": 1 / 0.0003048,
        "in": 1 / 0.0000254,
        "m": 1000,
        "cm": 100000,
        "mm": 1000000
    },
    "m": {
        "mi": 1 / 1609.344,
        "yd": 1 / 0.9144,
        "ft": 1 / 0.3048,
        "in": 1 / 0.0254,
        "km": 0.001,
        "cm": 100,
        "mm": 1000
    },
    "cm": {
        "mi": 1 / 160934.4,
        "yd": 1 / 91.44,
        "ft": 1 / 30.48,
        "in": 1 / 2.54,
        "km": 0.00001,
        "m": 0.01,
        "mm": 10
    },
    "mm": {
        "mi": 1 / 1609344,
        "yd": 1 / 914.4,
        "ft": 1 / 304.8,
        "in": 1 / 25.4,
        "km": 0.000001,
        "mm": 0.001,
        "cm": 0.1
    }
}

weight = {
    "hello": "world"
}

temp = {
    "c": {
        "f": lambda c: 1.8 * c + 32,
        "k": lambda c: c + 273.15
    },
    "f": {
        "c": lambda f: (5 / 9) * (f - 32),
        "k": lambda f: ((5 / 9) * (f - 32)) + 273.15
    },
    "k": {
        "f": lambda k: 1.8 * (k - 273.15) + 32,
        "c": lambda k: k - 273.15
    }
}

types = {
    "length": length,
    "weight": weight,
    "temp": temp
}