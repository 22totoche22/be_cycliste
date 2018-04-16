conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Les clubs",0)
    result += club()
    result += template.footer(chemin)
    return result


def club():
    vclub = '''
           <section id="clubs">

            <h2>Liste des clubs sportifs de l'ENAC</h2>
            <table class="table" data-toggle="table"   data-search="true" 
                   data-pagination="true"  data-page-size="3">
                <thead>
                    <tr>
                        <th data-field="col1" data-sortable="true">Club</th>
                        <th data-field="col2" data-sortable="true">Responsable</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Foot</td>
                        <td>M. Potogoal - IENAC17</td>
                    </tr>

                    <tr>
                        <td>Tennis</td>
                        <td>Melle Baballe - IESSA 16</td>
                    </tr>

                    <tr>
                        <td>Rugby</td>
                        <td>M. Ovale - TSA 17B</td>
                    </tr>

                    <tr>
                        <td>Ski</td>
                        <td>Melle Piquet - EPL 16</td>
                    </tr>

                </tbody>

            </table>
		</section>
             '''
    return vclub
