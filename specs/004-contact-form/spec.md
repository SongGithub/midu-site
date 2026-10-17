# Contact form

Requested by Song on 17 October 2026; direct email delivery selected in chat.

## Requirements
- Preserve the public site's branding, static hosting and existing contact links.
- Let visitors choose Recruitment opportunity or Business collaboration.
- Require name, email and a message; phone and organisation are optional.
- Explain that contact details are used to respond and FormSubmit processes delivery.
- Deliver submissions privately to the existing published address, songjin@hotmail.com.
- Never commit submissions, include personal information in analytics or store drafts in browser storage.
- Use accessible labels, native validation, mobile layouts and a working no-JavaScript path.

## Implementation decision
Use an HTTPS native POST to FormSubmit, which supports static GitHub Pages. Retain its default CAPTCHA and confirmation page. The owner's first submission requires email activation. Until activation and an actual received test are verified, email delivery must be described as pending verification. Existing mailto and LinkedIn links remain fallback routes.

## Verification
Check required fields, radio grouping, optional phone, HTTPS action, privacy notice, absence of analytics capture, existing analytics tests and the public-only build. Verify deployment separately from inbox delivery. Owner activation cannot be inferred from an HTTP success response.
