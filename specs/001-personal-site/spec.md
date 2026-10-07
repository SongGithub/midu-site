# Feature Specification: Midu Personal Site

**Feature Branch**: No branch created; specification is on `main`  
**Created**: 2026-10-07  
**Status**: Draft for review  
**Input**: [Shared planning conversation](https://chatgpt.com/share/6ac62580-cfa4-83ec-92f8-687a8c41d2d0) and the request to capture its requirements in Spec Kit.

## Objective and Scope

Create a small public site for Song at a domain to be confirmed. Its first job is to help a prospective employer understand Song's AI and platform engineering work through specific examples. Its second job is to let a potential business client understand the workflow problems Song could help with and make contact. LinkedIn can direct visitors to deeper evidence on the site.

The first release covers a landing page, selected work, a concise background, and contact paths. Technical notes may be added when useful. It does not require a publishing schedule, a consulting company identity, a booking system, an AI chat assistant, or a custom email service.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Employer evaluates Song (Priority: P1)

A hiring manager opens the site from a CV or LinkedIn profile and wants to understand who Song is, what roles fit, and what Song has built.

**Why this priority**: Employer credibility is the immediate purpose of the site.

**Independent Test**: A reviewer who has not met Song can use only the site to identify his professional focus and inspect at least one concrete project.

**Acceptance Scenarios**:

1. **Given** a first-time visitor, **when** they open the landing page, **then** they can identify Song by name, understand his AI/platform engineering focus, and find selected work within 60 seconds.
2. **Given** a selected project, **when** the visitor opens it, **then** they can see the problem, Song's contribution, the approach, evidence or outcome, and an approved demo or source link if available.
3. **Given** a visitor who wants to verify background, **when** they look for professional profiles or a CV, **then** the approved links or document are clearly available.

---

### User Story 2 - Business prospect evaluates fit (Priority: P2)

A small or medium business visitor wants to know whether Song can help improve a repetitive, knowledge-heavy workflow using AI and how to start a conversation.

**Why this priority**: The site should support testing a consulting offer without claiming a mature consultancy exists.

**Independent Test**: A business visitor can find a plain-language explanation of the problem area, see relevant evidence, and reach a contact method.

**Acceptance Scenarios**:

1. **Given** a business visitor, **when** they read the site, **then** they can identify the proposed focus as practical AI-assisted workflow improvement, with examples rather than a broad list of services.
2. **Given** a visitor interested in discussing a workflow, **when** they choose to contact Song, **then** they can use an approved contact method without creating an account.
3. **Given** that no paid consulting case study has been approved, **when** the site describes Song's work, **then** it does not imply prior client results or an established firm.

---

### User Story 3 - Song maintains the site (Priority: P3)

Song wants to add or revise a project or technical note when there is meaningful new evidence, without maintaining a frequent blog or complex content process.

**Why this priority**: The site should remain useful during a job search and inexpensive to maintain.

**Independent Test**: Song can update one project entry and publish the change using the documented workflow, with no unrelated page edits.

**Acceptance Scenarios**:

1. **Given** a new approved project detail, **when** Song updates the entry, **then** it appears in the selected work area and its dedicated page if one exists.
2. **Given** no new article, **when** months pass, **then** the site still presents complete core information without a visibly stale posting schedule.

### Edge Cases

- If a project has no public repository, benchmark, or demo, the page accurately explains the available evidence and omits unavailable links.
- If a proposed project is still an idea or prototype, the site labels its stage clearly.
- If a contact address, CV, or external profile is not approved, the site omits the action instead of showing a placeholder or broken link.
- If DNS for `midu.com.au` is not active at launch, the site can be previewed and reviewed at a temporary address before the domain is connected.
- On narrow screens and with keyboard or assistive technology, core content and contact paths remain usable.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The landing page MUST state Song's name, professional focus, and the kinds of work he does in clear language.
- **FR-002**: The site MUST give employers a direct route from the landing page to selected work and professional background.
- **FR-003**: The initial release MUST present at least one project with a verified problem, Song's contribution, approach, and evidence or outcome. Target three strong projects when approved material exists; do not invent content to reach that number.
- **FR-004**: Every project MUST distinguish completed work, prototypes, and planned work, and MUST only link to public demos or source that Song approves.
- **FR-005**: The site MUST provide a concise background or CV route and approved LinkedIn and GitHub links when available.
- **FR-006**: The site MUST explain the potential business offer as practical AI-assisted improvement to a specific workflow and provide an approved contact route.
- **FR-007**: The employer and business paths MUST share truthful project evidence while making each audience's next step clear.
- **FR-008**: Song MUST be able to add optional technical notes without a required posting frequency or an empty blog section on the initial release.
- **FR-009**: Navigation and content MUST work on common desktop and mobile screen sizes and support keyboard use and readable text.
- **FR-010**: The first release MUST avoid collecting visitor data beyond what is necessary for its approved contact method; any later form or analytics addition requires a documented purpose and handling decision.
- **FR-011**: All public claims, links, and contact details MUST be verified before publication.

### Key Entities

- **Profile**: Song's approved name, positioning, background, and contact paths.
- **Project**: Title, stage, problem, Song's contribution, approach, evidence or outcome, and approved external links.
- **Technical note**: Optional dated explanation of a real engineering decision or result, linked to a project where relevant.
- **Audience path**: Navigation and calls to action that guide either an employer or a potential client to relevant evidence and contact.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a five-person review, at least four first-time visitors can state Song's professional focus and find a project example within 60 seconds.
- **SC-002**: In a five-person employer review, at least four can identify Song's contribution and the evidence for one featured project within three minutes.
- **SC-003**: In a five-person business review, at least four can describe the type of workflow Song proposes to help with and find a contact route within two minutes.
- **SC-004**: Every published project, profile, contact, and external link passes a prelaunch accuracy check by Song; no placeholder or broken links remain.
- **SC-005**: The core employer and business journeys can be completed on desktop and mobile screens using keyboard navigation where relevant.
- **SC-006**: After initial publication, Song can revise a project or add a note in one focused session without altering unrelated content.

## Assumptions

- Song has purchased `midu.com.au`. DNS now serves the old blog's CNAME, while the apex is not connected to this new site. Site development and preview do not depend on the apex DNS being ready.
- Song's current job search makes employer evaluation the priority. The consulting offer is exploratory until Song validates demand and approves its wording.
- Project names and descriptions in the shared chat are examples, not verified portfolio facts. Song will supply or approve actual public project details, outcomes, CV, profile links, and contact details.
- A simple contact link is sufficient for the first release. Domain email, booking, forms, analytics, and an AI assistant require separate decisions.
- Technical notes are optional. No article count or publication cadence is required.

## Decisions Needed Before Publication

1. Confirm the public name, headline, and precise roles or problems to emphasize.
2. Select the first project or projects and provide approved evidence, results, images, demo links, and source links.
3. Confirm the public CV/profile links and contact method.
4. Confirm DNS and hosting arrangements for `midu.com.au` and whether the business-facing offer should invite conversations immediately.
