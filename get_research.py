import os
import sys
from get_news import load_index_page, save_index_page


def load_research_page(research_page_name):
    found_section = False
    research = []
    num_items = 0
    page = []
    with open(research_page_name, 'r') as in_f:
        for line in in_f:
            page.append(line)
    return get_research_items(page, max_num_items=5)

def get_research_items(page, max_num_items=5):
    found_section = False
    inside_research_topic = False
    num_items = 0
    research = []

    for i in range(len(page)):
        line = page[i]
        if not found_section:
            if 'research_section' in line:
                found_section = True
        else:
            if not inside_research_topic:
                if '<tr>' in line:
                    inside_research_topic = True
            else:
                if '</tr>' in line:
                    inside_research_topic = False
                    num_items += 1
                research.append(line)
        if 'end_section' in line or num_items > max_num_items:
            research.append('</tbody>\n</table>\n')
            return research
    return research


def main(args):
    pre_index, post_index = load_index_page(args.INDEX_PAGE, 'research')
    research = load_research_page(args.RESEARCH_PAGE)
    new_index = pre_index + research + post_index
    save_index_page(args.INDEX_PAGE, new_index)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('INDEX_PAGE')
    parser.add_argument('RESEARCH_PAGE')
    main(parser.parse_args())
