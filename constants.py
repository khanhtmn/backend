import enum

class ClassEnum(str, enum.Enum):
    """
    Class defining enums for class year
    used in tables
    """

    M19 = "Class of 2019"
    M20 = "Class of 2020"
    M21 = "Class of 2021"
    M22 = "Class of 2022"
    M23 = "Class of 2023"
    M24 = "Class of 2024"
    M25 = "Class of 2025"
    M26 = "Class of 2026"


class CollegeEnum(str, enum.Enum):
    """
    Class defining enums for majors and minors
    used in tables
    """

    CS = "Computational Sciences"
    BS = "Business"
    NS = "Natural Sciences"
    AH = "Arts & Humanities"
    SS = "Social Sciences"
    NA = "NA"


class ConcentrationEnum(str, enum.Enum):
    """
    Class defining enums for concentrations
    used in tables
    """

    APS = "Applied Problem Solving"
    AL = "Arts and Literature"
    BM = "Brand Management"
    CO = "Cells and Organisms"
    CBB = "Cognition, Brain, and Behavior"
    CTA = "Computational Theory and Analysis"
    CSAI = "Computer Science and Artificial Intelligence"
    CKD = "Contemporary Knowledge Discovery"
    DSS = "Data Science and Statistics"
    DS = "Designing Societies"
    ES = "Earth's Systems"
    ECS = "Economics and Society"
    EASS = "Empirical Approaches to the Social Sciences"
    EM = "Enterprise Management"
    HFC = "Historical Forces"
    HAN = "Humanities Analyses"
    HAP = "Humanities Applications"
    HFD = "Humanities Foundations"
    MOC = "Managing Operational Complexity"
    MATH = "Mathematics"
    MA = "Molecules and Atoms"
    NBV = "New Business Ventures"
    PEL = "Philosophy, Ethics, and the Law"
    PGS = "Politics, Government, and Society"
    PSCS = "Problem Solving in Complex Systems"
    RANS = "Research Analyses in Natural Science"
    SG = "Scalable Growth"
    SF = "Strategic Finance"
    TFNS = "Theoretical Foundations of Natural Science"
    TASS = "Theory and Analysis in the Social Sciences"
    CSC = "Custom / Special concentration"
    NA = "NA"


class RoleEnum(str, enum.Enum):
    """
    Class defining enums for professor and student role
    used in tables
    """

    advisor = "Advisor"
    student = "Student"

    # Consider having admin role


class FeatureEnum(str, enum.Enum):
    """
    Class defining enums for project features
    used in tables
    """

    creative = "Creative (e.g., writing, art)"
    primary_research = "Primary research (e.g., with a research group)"
    secondary_research = "Secondary research (e.g., literature review with analysis/synthesis and proposal for future work)"
    replication = "Replication"
    interview_survey = "Interview/survey"
    data_analysis = "Data analysis"
    journalism = "Journalism"
    philosophical = "Philosophical analysis"
    policy = "Policy analysis/proposal"
    education = "Educational curriculum/materials"
    business = "Business plan"
    podcast = "Podcast"
    app = "App"
    other = "Other"


class HSREnum(str, enum.Enum):
    """
    Class defining enums for HSR review status
    used in tables
    """

    not_yet = "Have not submitted a description yet"
    awaiting = "Submitted a brief description, awaiting reply"
    revising = "Revising based on HSR committee feedback"
    not_reviewed = "Reviewed by HSR committee: *NOT* HSR"
    reviewed = "Reviewed by HSR committee: Is HSR, possibly exempt"
    submitted = "Application for exemption submitted to IRB (no later than April 1, 2021)"
    confirmed = "Confirmed exempt by IRB (no later than Sept 1, 2021)"
    not_granted = "Exempt status not granted (must pursue other project)"
    na = "N/A (project does NOT involve interacting with any people and/or their information)"
    other = "Other"