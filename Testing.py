from task_3 import app

def test_my_dashboard_title(dash_duo):
    dash_duo.start_server(app)

    title_element = dash_duo.find_element('h1')

    assert title_element.text == 'Pink Morsel Sales Dashboard'

def test_my_chart_exists(dash_duo):
    dash_duo.start_server(app)

    chart_element = dash_duo.find_element('#sales-line-chart')

    assert chart_element is not None

def test_my_picker_exists(dash_duo):
    dash_duo.start_server(app)

    picker_element = dash_duo.find_element('#region-filter')

    assert picker_element is not None

    


    


