from dataclasses import asdict

from jd_parser.extractor import extract_title, extract_skills, extract_years
from jd_parser.io_utils import read_text, save_json
from jd_parser.models import JobInfo


def main() -> None:
    try:
        text = read_text("jd.txt")
    except FileNotFoundError:
        print("找不到 jd.txt，请先把 JD 文本放到项目根目录")
        return

    job = JobInfo(
        title=extract_title(text),
        skills=extract_skills(text),
        years_required=extract_years(text),
    )

    print(job.summary())
    save_json(asdict(job), "output.json")
    print("已保存到 output.json")


if __name__ == "__main__":
    main()