from collections import OrderedDict

__all__ = [
    'month_name', 'month_name_dev', 'month_number_dev', 'ENG_TO_DEV_DIGITS',
    'BS_YEAR_TO_MONTHS'
]

month_name = [
    '', 'Baisakh', 'Jestha', 'Ashadh', 'Shrawan', 'Bhadra', 'Ashwin', 'Kartik',
    'Mangsir', 'Poush', 'Magh', 'Falgun', 'Chaitra']
month_name_dev = [
    '', 'वैशाख', 'जेष्ठ', 'आषाढ़', 'श्रावण', 'भाद्र', 'आश्विन', 'कार्तिक',
    'मंसिर', 'पौष', 'माघ', 'फाल्गुन', 'चैत्र']
month_number_dev = ['', '१', '२', '३', '४', '५', '६', '७', '८', '९', '१०', '११', '१२']

ENG_TO_DEV_DIGITS = {
    0: '०', 1: '१', 2: '२', 3: '३', 4: '४', 5: '५', 6: '६', 7: '७', 8: '८', 9: '९'
}

# The keys are years in Bikram Samwat and the values are
# tuple containing the number of days for each month.
# The first item is None for consistency.
BS_YEAR_TO_MONTHS = OrderedDict((
    (2000, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2001, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2002, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2003, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2004, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2005, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2006, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2007, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2008, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31)),
    (2009, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2010, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2011, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2012, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30)),
    (2013, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2014, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2015, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2016, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30)),
    (2017, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2018, (None, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2019, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2020, (None, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2021, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2022, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30)),
    (2023, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2024, (None, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2025, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2026, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2027, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2028, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2029, (None, 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30)),
    (2030, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2031, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2032, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2033, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2034, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2035, (None, 30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31)),
    (2036, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2037, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2038, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2039, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30)),
    (2040, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2041, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2042, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2043, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30)),
    (2044, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2045, (None, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2046, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2047, (None, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2048, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2049, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30)),
    (2050, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2051, (None, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2052, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2053, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30)),
    (2054, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2055, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2056, (None, 31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30)),
    (2057, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2058, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2059, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2060, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2061, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2062, (None, 30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31)),
    (2063, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2064, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2065, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2066, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31)),
    (2067, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2068, (None, 31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2069, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2070, (None, 31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30)),
    (2071, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2072, (None, 31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30)),
    (2073, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31)),
    (2074, (None, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2075, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2076, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30)),
    (2077, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31)),
    (2078, (None, 31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2079, (None, 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30)),
    (2080, (None, 31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30)),
    (2081, (None, 31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30)),
    (2082, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30)),
    (2083, (None, 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30)),
    (2084, (None, 31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30)),
    (2085, (None, 31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30)),
    (2086, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30)),
    (2087, (None, 31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30)),
    (2088, (None, 30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30)),
    (2089, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30)),
    (2090, (None, 30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30)),
))
