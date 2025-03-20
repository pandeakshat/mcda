/*
 * @file Theme configuration
 */
import { defineConfig } from './src/helpers/config-helper';

export default defineConfig({
  lang: 'en-US',
  site: '',
  avatar: '/avatar.png',
  title: 'MCDA ',
  description: 'Multiple Criteria Decision Analysis - An Interactive Platform.',
  lastModified: true,
  readTime: true,
  footer: {
    copyright: '© 2025 pandeakshat',
  },
  socialLinks: [
    {
      icon: 'github',
      link: 'https://github.com/pandeakshat/'
    },
]
});