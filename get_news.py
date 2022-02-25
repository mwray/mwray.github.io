import os
import sys

def load_index_page(index_page_name, section_name):
    start_identifier = f'{section_name}_section'
    end_identifier = f'end_{section_name}'

    pre_index = []
    post_index = []
    found_section = False
    in_section = False
    with open(index_page_name, 'r') as in_f:
        for line in in_f:
            if not found_section:
                if start_identifier in line:
                    found_section = True
                    in_section = True
                    pre_index.append(line)
                else:
                    pre_index.append(line)
            else:
                if end_identifier in line:
                    in_section = False
                    post_index.append(line)
                else:
                    if not in_section:
                        post_index.append(line)
    return pre_index, post_index


def save_index_page(index_page_name, contents):
    with open(index_page_name, 'w') as out_f:
        for line in contents:
            out_f.write(line)


def load_news_page(news_page_name):
    found_section = False
    news = []
    num_items = 0
    with open(news_page_name, 'r') as in_f:
        for line in in_f:
            if not found_section:
                if 'news_section' in line:
                    found_section = True
            else:
                if 'end_section' in line or num_items > 8:
                    news.append('</ul>\n')
                    return news
                else:
                    news.append(line)
                    num_items += 1
    return news


def main(args):
    pre_index, post_index = load_index_page(args.INDEX_PAGE, 'news')
    news = load_news_page(args.NEWS_PAGE)
    new_index = pre_index + news + post_index
    save_index_page(args.INDEX_PAGE, new_index)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('INDEX_PAGE')
    parser.add_argument('NEWS_PAGE')
    main(parser.parse_args())
