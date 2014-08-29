class FocusArea():
    def __init__(self):
        self.focus_area = ''


class CompetencyArea():
    def __init__(self, focus_area):
        self.focus_area = focus_area
        self.competency_area = ''

class PerformanceIndicator():
    def __init__(self, level, competency_area):
        self.level = level
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


def show_all_standards():
    current_fa = ''
    current_ca = ''
    for ca in competency_areas:
        if ca.focus_area != current_fa:
            current_fa = ca.focus_area
            print('\n' + current_fa.focus_area.title())
        print('\n  ' + ca.competency_area.title())
        # Run through pi's, pull relevant ones.
        #  Would be much better in a db, running a query!
        current_level = ''
        for pi in performance_indicators:
            if pi.competency_area == ca:
                if pi.level != current_level:
                    current_level = pi.level
                    print('\n    Level %s' % current_level)
                print('      ' + pi.performance_indicator.capitalize())


def auto_gen_all_standards(prefix = ''):
    """Dump the standards into a markdown file.
    Prefix allows generation of a simple checklist.
      Prefixing underscores gives space to record scores etc.
    """
    if prefix:
        filepath = '../auto_generated_files/all_standards_simple_format_prefix_' + prefix.strip() + '.md'
    else:
        filepath = '../auto_generated_files/all_standards_simple_format.md'
    with open(filepath, 'w') as f:
        f.write('Computer Science\n===\n')
        current_fa = ''
        current_ca = ''
        for ca in competency_areas:
            if ca.focus_area != current_fa:
                current_fa = ca.focus_area
                f.write('\n\n' + current_fa.focus_area.title() + '\n---\n\n')
            f.write('\n- ' + prefix + ca.competency_area.title())

            # Run through pi's, pull relevant ones.
            #  Would be much better in a db, running a query!
            levels = ['', '1', '2', '3']
            for level in levels:
                level_shown = False
                for pi in performance_indicators:
                    if pi.level == level and pi.competency_area == ca:
                        if not level_shown and level != '':
                            f.write('\n  - Level %s Performance Indicators:' % level)
                            level_shown = True
                        f.write('\n    - ' + prefix + pi.performance_indicator.capitalize())
                        


                            
    print("Generated file: all_standards_simple_format.md. prefix: %s" % prefix)
    # Create .docx version of md file.
    from subprocess import call
    #call(["pandoc", "/home/ehmatthes/development/projects/cs_standards/auto_generated_files/all_standards_simple_format.md -o all_standards_simple_format.docx"])


auto_gen_all_standards()
#auto_gen_all_standards(prefix='____ ')

