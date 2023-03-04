import pandas as pd


def build_table(df, color, font_size = 'medium', font_family = 'Century Gothic', text_align = 'left') -> str:
    """
    Copied from https://github.com/sbi-rviot/ph_table to simplify deployment
    """
    if df.empty:
      return ''
    # Reformat table_color as dict of tuples

    dict_colors = {
        'yellow_light' : ('#BF8F00', '2px solid #BF8F00', '#FFF2CC', '#FFFFFF'),
        'grey_light' : ('#808080', '2px solid #808080', '#EDEDED', '#FFFFFF'),
        'blue_light' : ('#305496', '2px solid #305496', '#D9E1F2', '#FFFFFF'),
        'orange_light' : ('#C65911', '2px solid #C65911', '#FCE4D6', '#FFFFFF'),
        'green_light' : ('#548235', '2px solid #548235', '#E2EFDA', '#FFFFFF'),
        'red_light' : ('#823535', '2px solid #823535', '#efdada', '#FFFFFF'),
        'yellow_dark' : ('#FFFFFF', '2px solid #BF8F00', '#FFF2CC', '#BF8F00'),
        'grey_dark' : ('#FFFFFF', '2px solid #808080', '#EDEDED', '#808080'),
        'blue_dark': ('#FFFFFF', '2px solid #305496', '#D9E1F2', '#305496'),
        'orange_dark' : ('#FFFFFF', '2px solid #C65911', '#FCE4D6', '#C65911'),
        'green_dark' : ('#FFFFFF', '2px solid #548235', '#E2EFDA', '#548235'),
        'red_dark' : ('#FFFFFF', '2px solid #823535', '#efdada', '#823535')
    }
    # Set color
    # oadding = up, right, down, left
    padding="0px 20px 0px 8px"
    even_background_color = '#FFFFFF'
    color, border_bottom, odd_background_color, header_background_color = dict_colors[color]

    a = 0
    while a != len(df):
        if a == 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = False, border = 0)
            # change format of header
            df_html_output = df_html_output.replace('<th>'
                                                    ,'<th style = "background-color: ' + header_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';color: ' + color
                                                    + ';text-align: ' + text_align
                                                    + ';border-bottom: ' + border_bottom
                                                    + ';padding: ' + padding + '">')

            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding + '">')

            body = """<p>""" + format(df_html_output)

            a = 1

        elif a % 2 == 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = False, header = False)

            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding + '">')

            body = body + format(df_html_output)

            a += 1

        elif a % 2 != 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = False, header = False)

            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + even_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding + '">')

            body = body + format(df_html_output)

            a += 1

    body = body + """</p>"""

    body = body.replace("""</td>
    </tr>
  </tbody>
</table>
            <table border="1" class="dataframe">
  <tbody>
    <tr>""","""</td>
    </tr>
    <tr>""").replace("""</td>
    </tr>
  </tbody>
</table><table border="1" class="dataframe">
  <tbody>
    <tr>""","""</td>
    </tr>
    <tr>""")

    return body


def get_greeting(empty: bool = False) -> str:
    if empty:
        n_files = 'geen'
    else:
        n_files = 'de volgende'
    bericht = f'<h2>Beste, {n_files} bestanden waren geüpload in de afgelopen 24 uur.</h2>'
    return bericht

if __name__ == '__main__':
    data = {'Tijd geüpload': [1,2,3,4],
            'Bedrijfsnaam': ['DC', 'DC', 'SC', 'SC'],
            'Omschrijving': ['factuur1', 'factuur2', 'factuur12', 'factuur13']
            }
    out = pd.DataFrame(data)
    bericht = get_greeting()
    styled_html = bericht + build_table(out, color='blue_light')
    with open('styled.html', 'w') as f:
        f.write(styled_html)
