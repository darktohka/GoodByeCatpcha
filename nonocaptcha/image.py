#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" ***IN TESTING*** """

class SolveImage(object):
    def __init__(self, frames, check_detection, proxy, log):
        self.checkbox_frame, self.image_frame = frames
        self.check_detection = check_detection
        self.proxy = proxy
        self.log = log
        self.detected = False

    async def solve_by_image(self):
        """Go through procedures to solve image"""
        
        title = await self.get_image_title()
        return title

    async def get_image_title(self):
        """Something, something... something"""

        image_title_element = (
            'document.getElementsByClassName("rc-imageselect-desc'
            '")[0]'
        )

        if await self.image_frame.evaluate(
            f"typeof {image_title_element} === 'undefined'"
        ):
            image_title_element = (
                'document.getElementsByClassName("rc-imageselect-desc-no-'
                'canonical")[0]'
            )

        return await self.image_frame.evaluate(
            f"{image_title_element}.innerText"
            f".replace( /.*\\n(.*)\\n.*/,'$1');"
        )