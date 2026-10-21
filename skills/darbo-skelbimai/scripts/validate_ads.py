"""Deterministic job-ad status helpers; no browsing or network calls."""
from datetime import datetime
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

TRACKING = {'fbclid','gclid','utm_source','utm_medium','utm_campaign','utm_term','utm_content'}

def canonical_url(url):
    u = urlsplit(url.strip())
    if u.scheme not in {'https', 'http'} or not u.netloc:
        raise ValueError('Invalid advertisement URL')
    query = urlencode(sorted((k,v) for k,v in parse_qsl(u.query) if k.lower() not in TRACKING))
    return urlunsplit((u.scheme.lower(),u.netloc.lower(),u.path.rstrip('/') or '/',query,''))

def status(evidence, checked_at):
    """active, expired or unverified; checked_at timezone-aware datetime."""
    if checked_at.tzinfo is None:
        raise ValueError('checked_at must be timezone-aware')
    if evidence.get('closed') is True or evidence.get('accepting_applications') is False:
        return 'expired'
    deadline = evidence.get('deadline')
    if deadline:
        due = datetime.fromisoformat(deadline.replace('Z','+00:00'))
        if due.tzinfo is None:
            raise ValueError('deadline needs timezone')
        if due < checked_at:
            return 'expired'
    if not all(evidence.get(k) for k in ('page_opened','matching_company','matching_title')):
        return 'unverified'
    if evidence.get('accepting_applications') is True:
        return 'active'
    if deadline and due >= checked_at and evidence.get('apply_action_verified') is True:
        return 'active'
    return 'unverified'

def deduplicate(records):
    seen=set(); out=[]
    for item in records:
        key=(item.get('employer','').casefold().strip(),item.get('title','').casefold().strip(),item.get('city','').casefold().strip())
        url=canonical_url(item['url'])
        if url in seen or key in seen: continue
        seen.update((url,key)); out.append(item)
    return out
