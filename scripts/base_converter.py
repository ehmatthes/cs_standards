class FocusArea():
    def __init__(self):
        self.focus_area = ''


class CompetencyArea():
    def __init__(self, focus_area):
        self.focus_area = focus_area
        self.competency_area = ''

class PerformanceIndicator():
    def __init__(self, level, competency_area):
        self.level = ''
        self.competency_area = competency_area
        self.performance_indicator = ''


# Open main standards file, and read in contents.
with open('../cs_standards.md') as fobj:
    lines = list(fobj)


focus_areas = []
competency_areas = []
current_level = ''
performance_indicators = []

for line in lines:
    
    if 'fa:' in line.lower():
        new_fa = FocusArea()
        # Should use a regex.
        new_fa.focus_area = line.lower().replace('fa:', '').strip()
        focus_areas.append(new_fa)

    if 'ca:' in line.lower():
        # Focus area for this competency area is the most recent focus area.
        new_ca = CompetencyArea(focus_areas[-1])
        new_ca.competency_area = line.lower().replace('- ca:', '').strip()
        competency_areas.append(new_ca)

    if '- level' in line.lower():
        # Set level for performance indicators to follow.
        number_location = line.find(':')
        current_level = line[number_location-1]

    if 'pi:' in line.lower():
        # Competency area for this performance indicator is the most recent ca.
        new_pi = PerformanceIndicator(current_level, competency_areas[-1])
        new_pi.performance_indicator = line.lower().replace('  - pi:', '').strip()
        performance_indicators.append(new_pi)


current_fa = ''
for ca in competency_areas:
    if ca.focus_area != current_fa:
        current_fa = ca.focus_area
        print('\n' + current_fa.focus_area.title())
    print('  ' + ca.competency_area.title())

for pi in performance_indicators:
    print(pi.performance_indicator.capitalize())
