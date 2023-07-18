question = "4 * <w>"
print(f"Original Question: {question}")

w = 2
l = 4
replaced_question = question.replace("<w>", str(w)).replace("<l>", str(l))
print(f"Replaced Question: {replaced_question}")

geo_eas_questions = ["Square with perimeter <x>, what is the width? ",
                     "Rectangle with perimeter <x>, length <l>, what is the width? ",
                     "Rectangle with perimeter <x>, width <w>, what is the length? ",
                     "Rectangle with width <w>, length <l>, what is the perimeter? "
                    ]

geo_eas_equations = {"4 * <w>" : "<x>",
                     "2 * (<w> + <l>)" : "<w>",
                     "2 * (<l> + <w>)" : "<l>",
                     "(<w> + <l>) * 2" : "<x>"
                    }