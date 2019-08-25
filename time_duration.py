import asyncio
import discord

async def time_duration(client, ctx, duration, time_wait):
    """
    Sends a message to the user saying the interval they have selected,
    along with getting the proper amount of seconds needed by the euler()
    in order to wait.
    """

    duration_long = ""  # Variable for the length of the interval provided in easier-to-read format.

    if duration == "d":  # If the user requested a wait interval of d for days:
        duration_long = "{} days".format(time_wait)  # Set duration_long to the singular format.
        time_wait = int(time_wait) * 86400  # Multiples time_wait by the amount of seconds in a day (86400)
    # Same comments from above apply to all the other statements below, except for time differences based on time requested by the user.
    elif duration == "h":
        duration_long = "{} hours".format(time_wait)
        time_wait = int(time_wait) * 3600
    elif duration == "m":
        duration_long = "{} minutes".format(time_wait)
        time_wait = int(time_wait) * 60
    elif duration == "s":
        duration_long = "{} seconds".format(time_wait)
        time_wait = int(time_wait) * 1
    else:
        duration_long = "{} hours".format(time_wait)
        time_wait = int(time_wait) * 3600

    if time_wait == 1:
        duration_long = duration_long[:-1]
    # Sends a message with the time interval interpreted to be easier-to-read.
    await client.send_message(ctx.message.channel, "You have started the random problem loop with a time interval of {}.".format(duration_long))

    return time_wait  # Return the time_wait variable
