def format_time(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    if hours > 0:
        return f"{int(hours)}h {int(minutes)}m {seconds:.3f}s"
    elif minutes > 0:
        return f"{int(minutes)}m {seconds:.3f}s"
    else:
        return f"{seconds:.3f}s"
