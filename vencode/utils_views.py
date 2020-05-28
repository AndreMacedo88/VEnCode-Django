def prepare_df(df):
    html_table = df.to_html(index=False)
    html_table = "\n".join(html_table.split('\n')[1:-1])
    return html_table
