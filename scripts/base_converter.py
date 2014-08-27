class FocusArea():
    def __init__(self):
        self.focus_area = ''


class CompetencyArea():
    def __init__(self, focus_area):
        self.focus_area = focus_area
        self.competency_area = ''

class PerformanceIndicator():
    def __init__(self, competency_area):
        self.level = '1'
        self.competency_area = competency_area
        self.performance_indicator = ''


# Open main standards file, and read in contents.
with open('../cs_standards.md') as fobj:
    lines = list(fobj)


focus_areas = []
competency_areas = []

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


current_fa = ''
for ca in competency_areas:
    if ca.focus_area != current_fa:
        current_fa = ca.focus_area
        print('\n' + current_fa.focus_area.title())
    print('  ' + ca.competency_area.title())

