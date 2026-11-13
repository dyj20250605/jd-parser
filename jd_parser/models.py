from dataclasses import dataclass, field
@dataclass
class JobInfo:
    title: str
    skills: list[str] = field(default_factory=list)
    years_required: int | None = None
    def summary(self) -> str:
        if self.years_required is None:
            return f"{self.title}（经验不限）， 技能{','.join(self.skills)}"
        else:
            return f"{self.title}（经验{self.years_required}年）， 技能{','.join(self.skills)}"
